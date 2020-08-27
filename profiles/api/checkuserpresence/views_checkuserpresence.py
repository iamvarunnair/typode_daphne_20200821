from rest_framework.views import APIView, Response
from rest_framework import status
from main.utilities.utility import validate_request_json, validate_json_with_schema_from_file
from apiauthentication.api.authenticateapi.views_authenticateapi import authenticate_api
from ...utilities.utility import check_user_pressence


class CheckUserPresenceAPI(APIView):
    """ Log in profile """
    @validate_request_json(choice=0)
    @authenticate_api
    def post(self, request):
        try:
            output_json = {}
            if validate_json_with_schema_from_file(
                'profiles\\api\\checkuserpresence\\schema_checkuserpresence.json',
                request.data['api_parameters']
            )['status'] == 0:
                if check_user_pressence(request.data['api_parameters']['user_name'])['status'] == 0:
                    return Response(data= {
                        'api_payload': {
                            'status': 1,
                            "message": "Welcome user, log in to continue.",
                        }
                    }, status=status.HTTP_200_OK)
                elif check_user_pressence(request.data['api_parameters']['user_name'])['status'] == 1:
                    return Response(data={
                        'api_payload': {
                            'status': 0,
                            "message": "New User, sign up to continue.",
                        }
                    }, status=status.HTTP_200_OK)
                else:
                    raise
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
