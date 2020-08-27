from rest_framework.views import APIView, Response
from rest_framework import status
from main.utilities.utility import validate_request_json, validate_json_with_schema_from_file
from apiauthentication.api.authenticateapi.views_authenticateapi import authenticate_api
from sessionmanagement.api.updatesessions.views_updatesessions import update_session
from ...models import ChatRequest
from django.db.models import Q


class RemoveChatContactAPI(APIView):
    """ Log in profile """
    @validate_request_json(choice=1)
    @authenticate_api
    @update_session(choice=0)
    def post(self, request):
        try:
            output_json = {}
            if validate_json_with_schema_from_file(
                'chat\\api\\removechatcontact\\schema_removechatcontact.json',
                request.data['api_parameters']
            )['status'] == 0:
                output_json['session_payload'] = request.data['session_payload']
                if ChatRequest.objects.filter(
                        Q(
                            requester_id=request.data['session_details']['profile_id'],
                            respondent_id=request.data['api_parameters']['profile_id']
                        ) | Q(
                            requester_id=request.data['api_parameters']['profile_id'],
                            respondent_id=request.data['session_details']['profile_id']
                        ), Q(status=2)).update(status=5):
                    output_json['api_payload'] = {
                        'status': 0,
                        'message': 'Successfully removed contact.'
                    }
                else:
                    output_json['api_payload'] = {
                        'status': 1,
                        'message': 'Failed to remove contact.',
                    }
                return Response(data=output_json, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
