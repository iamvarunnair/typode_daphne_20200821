from rest_framework.views import APIView, Response
from rest_framework import status
from main.utilities.utility import validate_request_json, validate_json_with_schema_from_file
from apiauthentication.api.authenticateapi.views_authenticateapi import authenticate_api
from sessionmanagement.api.updatesessions.views_updatesessions import update_session
from ...models import ChatRequest
from django.db.models import Q
from ...serializers import ChatRequestSerializer
from django.db import transaction


class SendChatRequestAPI(APIView):
    """ Log in profile """
    @validate_request_json(choice=1)
    @authenticate_api
    @update_session(choice=0)
    def post(self, request):
        try:
            output_json = {}
            if validate_json_with_schema_from_file(
                'chat\\api\\sendchatrequest\\schema_sendchatrequest.json',
                request.data['api_parameters']
            )['status'] == 0:
                output_json['session_payload'] = request.data['session_payload'],
                if ChatRequest.objects.filter(
                    Q(
                        requester_id=request.data['session_details']['profile_id'],
                        respondent_id=request.data['api_parameters']['send_to']
                    ) | Q(
                        requester_id=request.data['api_parameters']['send_to'],
                        respondent_id=request.data['session_details']['profile_id']
                    ), Q(status__in=[1, 2])
                ).exists():
                    output_json['api_payload'] = {
                        'status': 1,
                        'message': 'Failed to send request, it already exists.'
                    }
                else:
                    serialized_request = ChatRequestSerializer(data={
                        'requester_id': request.data['session_details']['profile_id'],
                        'respondent_id': request.data['api_parameters']['send_to'],
                        'status': 1
                    })
                    if serialized_request.is_valid():
                        with transaction.atomic():
                            serialized_request.save()
                            output_json['api_payload'] = {
                                'status': 0,
                                'message': 'Successfully request sent.'
                            }
                    else:
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                return Response(data=output_json, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
