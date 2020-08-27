from rest_framework.views import APIView, Response
from rest_framework import status
from main.utilities.utility import validate_request_json, validate_json_with_schema_from_file
from apiauthentication.api.authenticateapi.views_authenticateapi import authenticate_api
from sessionmanagement.api.updatesessions.views_updatesessions import update_session
from ...models import ChatRequest


class RespondToChatRequestAPI(APIView):
    """ Log in profile """
    @validate_request_json(choice=1)
    @authenticate_api
    @update_session(choice=0)
    def post(self, request):
        try:
            output_json = {}
            if validate_json_with_schema_from_file(
                'chat\\api\\respondtochatrequest\\schema_respondtochatrequest.json',
                request.data['api_parameters']
            )['status'] == 0:
                output_json['session_payload'] = request.data['session_payload']
                if request.data['api_parameters']['response'] == 0:         # for accepted
                    response = 2
                elif request.data['api_parameters']['response'] == 1:         # for rejected
                    response = 3
                if ChatRequest.objects.filter(
                        pk=request.data['api_parameters']['request_id'],
                        respondent_id=request.data['session_details']['profile_id'],
                        status=1).update(status=response):
                    output_json['api_payload'] = {
                        'status': 0,
                        'message': 'Successfully updated request.'
                    }
                else:
                    output_json['api_payload'] = {
                        'status': 1,
                        'message': 'Failed to update request.',
                    }
                return Response(data=output_json, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
