from rest_framework.views import APIView, Response
from main.utilities.utility import validate_request_json
from apiauthentication.api.authenticateapi.views_authenticateapi import authenticate_api


class LoginProfileAPI(APIView):
    """ Log in profile """
    @validate_request_json(type=0)
    @authenticate_api
    def post(self, request):
        return Response(data={'check': 'worked'}, status=200)
