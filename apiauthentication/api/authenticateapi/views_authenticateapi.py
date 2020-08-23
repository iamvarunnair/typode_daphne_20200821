from rest_framework.views import Response
from functools import wraps
from ...models import ApiTokens
from django.core.exceptions import ObjectDoesNotExist
from main.utilities.utility import read_from_json_file, validate_json


development_key = '3mLoEPlG2e9lDZxEOfonICpD2iHnAv3h'


def authenticate_api(function):
    @wraps(function)
    def wrapper_authenticate_api(self, request, *args, **kwargs):
        try:
            read_json = read_from_json_file(
                'apiauthentication\\api\\authenticateapi\\schema_authenticateapi.json')
            if request is not None and \
                'api_details' in request.data and \
                read_json['status'] == 0 and \
                    validate_json(read_json['payload'], request.data['api_details'])['status'] == 0:
                try:
                    if ApiTokens.objects.get(token_string__exact=request.data['api_details']['token_key']) and \
                            request.data['api_details']['development_key'] == development_key:
                        return function(self, request, *args, **kwargs)
                except ObjectDoesNotExist:
                    return Response(401)
            else:
                raise
        except Exception as err:
            return Response(status=400)
    return wrapper_authenticate_api
