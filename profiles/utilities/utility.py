from django.core.exceptions import ObjectDoesNotExist
from ..models import Profile
from sessionmanagement.utilities.utility import create_session_from_profile_id


def check_user_pressence(user_name):
    output_json = {}
    try:
        Profile.objects.get(
            user_name__exact=user_name,
            status=1
        )
        output_json = {
            'status': 0,
            "message": "User exists.",
        }
    except ObjectDoesNotExist:
        output_json = {
            'status': 1,
            "message": "User doesn't exist",
        }
    finally:
        return output_json


def login_profile(user_name, password):
    output_json = {}
    try:
        user = Profile.objects.get(
            user_name__exact=user_name,
            password__exact=password,
            status=1
        )
        created_session = create_session_from_profile_id(
            user.profile_id)
        if created_session['status'] == 0:
            output_json = {
                'status': 0,
                'message': 'Successfully profile logged in.',
                'payload': created_session
            }
        else:
            output_json = {
                'status': 1,
                'message': 'Failed to log profile in.'
            }
    except ObjectDoesNotExist:
        output_json = {
            'status': 1,
            'message': 'Failed to log profile in.'
        }
    finally:
        return output_json
