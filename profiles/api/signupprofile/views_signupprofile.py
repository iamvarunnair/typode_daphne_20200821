from rest_framework.views import APIView, Response
from rest_framework import status
from main.utilities.utility import validate_request_json, validate_json_with_schema_from_file
from apiauthentication.api.authenticateapi.views_authenticateapi import authenticate_api
from ...utilities.utility import check_user_pressence
from ...serializers import ProfileSerializer
from ...models import Avatar
from sessionmanagement.utilities.utility import create_session_from_profile_id
from django.db import transaction


class SignupProfileAPI(APIView):
    """ Log in profile """
    @validate_request_json(choice=0)
    @authenticate_api
    def post(self, request):
        try:
            output_json = {}
            if validate_json_with_schema_from_file(
                'profiles\\api\\signupprofile\\schema_signupprofile.json',
                request.data['api_parameters']
            )['status'] == 0 and \
                    Avatar.objects.filter(pk=request.data['api_parameters']['avatar_id']).exists():
                if check_user_pressence(
                    request.data['api_parameters']['user_name']
                )['status'] == 1:           # status 1 equates failure, user doesn't exist
                    serialized_profile = ProfileSerializer(data={
                        'user_name': request.data['api_parameters']['user_name'],
                        'password': request.data['api_parameters']['password'],
                        'avatar_id': request.data['api_parameters']['avatar_id'],
                        'status': 1
                    })
                    if serialized_profile.is_valid():
                        with transaction.atomic():
                            serialized_profile.save()
                            logged_user = create_session_from_profile_id(
                                serialized_profile.data['profile_id'])
                            output_json['session_payload'] = logged_user['payload']
                            output_json['api_payload'] = {
                                'status': 0,
                                'message': 'Successfully profile signed up and logged in.'
                            }
                    else:
                        output_json['api_payload'] = {
                            'status': 1,
                            'message': 'Failed to sign up profile.'
                        }
                else:
                    output_json['api_payload'] = {
                        'status': 1,
                        'message': 'Failed to sign up profile. User already exists.'
                    }
                return Response(data=output_json, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
