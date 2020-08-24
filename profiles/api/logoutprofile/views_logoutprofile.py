from rest_framework.views import APIView, Response
from rest_framework import status
from main.utilities.utility import validate_request_json
from apiauthentication.api.authenticateapi.views_authenticateapi import authenticate_api
from sessionmanagement.api.updatesessions.views_updatesessions import update_session


class LogoutProfileAPI(APIView):
    """ Log in profile """
    @validate_request_json(choice=1)
    @authenticate_api
    @update_session(choice=1)
    def post(self, request):
        try:
            output_json = {
                'api_payload': {
                    'status': 0,
                    'message': 'Successfully logged user out.'
                }
            }
            return Response(data=output_json, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
