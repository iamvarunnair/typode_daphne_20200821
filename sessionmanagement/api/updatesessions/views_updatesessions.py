from rest_framework.views import Response
from functools import wraps
from main.utilities.utility import validate_json_with_schema_from_file
from rest_framework import status
from django.db import transaction
from django.utils.crypto import get_random_string
from django.core.exceptions import ObjectDoesNotExist
from ...models import Session, SessionStatus
from ...serializers import SessionSerializer


def update_session(choice):
    """
    choice
    0 for updating session
    1 for updating session and change status to 2(Inactive) for logging user out.
    """
    def decorator_update_session(function):
        @wraps(function)
        def wrapper_update_session(self, request, *args, **kwargs):
            try:
                if validate_json_with_schema_from_file(
                    'sessionmanagement\\api\\updatesessions\\schema_updatesessions.json',
                    request.data['session_details']
                )['status'] == 0:
                    try:
                        if Session.objects.filter(
                            pk=request.data['session_details']['session_id'],
                            profile_id=request.data['session_details']['profile_id'],
                            status=1
                        ).exists():
                            with transaction.atomic():
                                session_to_update = Session.objects.select_for_update().get(
                                    pk=request.data['session_details']['session_id'],
                                    profile_id=request.data['session_details']['profile_id'],
                                    session_key__exact=request.data['session_details']['session_key'],
                                    status=1
                                )
                                session_to_update.session_key = get_random_string(
                                    length=32)
                                if choice == 1:
                                    session_to_update.status = SessionStatus.objects.get(
                                        pk=2)
                                session_to_update.save()
                                request.data['session_payload'] = {
                                    'status': 0,
                                    'message': 'Successfully updated session.',
                                    'payload': {
                                        'profile_id': session_to_update.profile_id.profile_id,
                                        'session_id': session_to_update.session_id,
                                        'session_key': session_to_update.session_key,
                                    }
                                }
                                return function(self, request, *args, **kwargs)
                        else:
                            raise
                    except ObjectDoesNotExist:
                        with transaction.atomic():
                            session_to_update = Session.objects.select_for_update().get(
                                pk=request.data['session_details']['session_id'],
                                profile_id=request.data['session_details']['profile_id'],
                                status=1
                            )
                            session_to_update.status = SessionStatus.objects.get(
                                pk=2)
                            session_to_update.session_key = get_random_string(
                                length=32)
                            session_to_update.save()
                            return Response(data={
                                'session_payload': {
                                    'status': 1,
                                    'message': 'Failed to update session, closed.',
                                }
                            }, status=status.HTTP_200_OK)
                    except Exception:
                        return Response(data={
                            'session_payload': {
                                'status': 1,
                                'message': 'Session does not exist.',
                            }
                        }, status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            except Exception as err:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return wrapper_update_session
    return decorator_update_session
