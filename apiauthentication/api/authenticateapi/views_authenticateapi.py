from rest_framework.views import Response
from functools import wraps
from ...models import ApiTokens
from django.core.exceptions import ObjectDoesNotExist
from main.utilities.utility import validate_json_with_schema_from_file
from rest_framework import status

development_key = '3mLoEPlG2e9lDZxEOfonICpD2iHnAv3h'


def authenticate_api(function):
    @wraps(function)
    def wrapper_authenticate_api(self, request, *args, **kwargs):
        try:
            if validate_json_with_schema_from_file(
                'apiauthentication\\api\\authenticateapi\\schema_authenticateapi.json',
                request.data['api_details']
            )['status'] == 0:
                try:
                    if ApiTokens.objects.get(token_string__exact=request.data['api_details']['token_key'], status=1) and \
                            request.data['api_details']['development_key'] == development_key:
                        request.data['authentication_payload'] = {
                            'status': 0,
                            'message': 'Successfully authenticated api.'
                        }
                        return function(self, request, *args, **kwargs)
                    else:
                        raise
                except ObjectDoesNotExist:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
                except Exception:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            else:
                raise
        except Exception as err:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return wrapper_authenticate_api
