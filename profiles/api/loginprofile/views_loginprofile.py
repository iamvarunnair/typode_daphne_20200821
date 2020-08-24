from rest_framework.views import APIView, Response
from rest_framework import status
from main.utilities.utility import validate_request_json, validate_json_with_schema_from_file
from apiauthentication.api.authenticateapi.views_authenticateapi import authenticate_api
from sessionmanagement.utilities.utility import create_session_from_profile_id
from sessionmanagement.api.updatesessions.views_updatesessions import update_session
from ...models import Profile
from django.core.exceptions import ObjectDoesNotExist


class LoginProfileAPI(APIView):
    """ Log in profile """
    @validate_request_json(choice=0)
    @authenticate_api
    def post(self, request):
        try:
            output_json = {
                'authentication_payload': request.data['authentication_payload'],
            }
            if validate_json_with_schema_from_file(
                'profiles\\api\\loginprofile\\schema_loginprofile.json',
                request.data['api_parameters']
            )['status'] == 0:
                try:
                    user = Profile.objects.get(
                        user_name__exact=request.data['api_parameters']['user_name'],
                        password__exact=request.data['api_parameters']['password']
                    )
                    created_session = create_session_from_profile_id(
                        user.profile_id)
                    if created_session['status'] == 0:
                        output_json['session_payload'] = created_session
                        output_json['api_payload'] = {
                            'status': 0,
                            'message': 'Successfully profile logged in.'
                        }
                    else:
                        output_json['api_payload'] = {
                            'status': 1,
                            'message': 'Failed to log profile in.'
                        }
                except ObjectDoesNotExist:
                    output_json['api_payload'] = {
                        'status': 1,
                        'message': 'Failed to log profile in.'
                    }
                finally:
                    return Response(data=output_json, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TempAPI(APIView):
    """ Log in profile """
    @validate_request_json(choice=1)
    @authenticate_api
    @update_session(choice=0)
    def post(self, request):
        output_json = {
            'authentication_payload': request.data['authentication_payload'],
            'session_payload': request.data['session_payload'],
        }
        return Response(data=output_json, status=status.HTTP_200_OK)
