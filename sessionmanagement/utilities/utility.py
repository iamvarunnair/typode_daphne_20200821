from ..models import Session
from profiles.models import Profile
from ..serializers import SessionSerializer
from django.utils.crypto import get_random_string
from django.db import transaction


def create_session_from_profile_id(profile_id):
    try:
        if Profile.objects.get(pk=profile_id, status=1):
            session_serialized = SessionSerializer(data={
                'profile_id': profile_id,
                'session_key': get_random_string(length=32),
                'status': 1
            })
            if session_serialized.is_valid():
                with transaction.atomic():
                    session_serialized.save()
                    return {
                        'status': 0,
                        'message': 'Successfully created session.',
                        'payload': {
                            'profile_id': session_serialized.data['profile_id'],
                            'session_id': session_serialized.data['session_id'],
                            'session_key': session_serialized.data['session_key'],
                        }
                    }
            else:
                raise
        else:
            raise
    except Exception:
        return {
            'status': 1,
            'message': 'Failed validated json with schema',
        }
