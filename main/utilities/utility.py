from jsonschema import Draft7Validator
from functools import wraps
from rest_framework.views import Response
import json

"""
[
    {
        'modla_name': ModalImpoted,
        'entries': [
            {
                'exact_field_name': 'value',
                'exact_field_name': 'value',
            },
            {
                'exact_field_name': 'value',
                'exact_field_name': 'value',
            },
            ...
        ]
    },
    ...
]
"""


def mass_insert_into_tables(input_data):
    for instance in input_data:
        if 'modal_name' in instance and 'entries' in instance and len(instance['modal_name'].objects.all()) == 0:
            for entry in instance['entries']:
                instance['modal_name'](**entry).save()
        else:
            raise Exception('modal_name and entries not in param')


"""
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "http://example.com/product.schema.json",
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "rollnumber": {"type": "number"},
        "marks": {"type": "number"},
    },
    "required": ["name", "rollnumber", "marks"],
    "additionalProperties": False,
}
"""


def validate_json(schema, jsonData):
    try:
        if Draft7Validator(schema).is_valid(jsonData):
            return {
                'status': 0,
                'message': 'Successfully validated json with schema',
            }
        else:
            raise
    except Exception as err:
        return {
            'status': 1,
            'message': 'Failed validated json with schema',
        }


def validate_request_json(type):
    """
    type
    0 for prelogin without session_details
    1 for postlogin with session_details
    """
    def decorator_validate_request_json(function):
        @wraps(function)
        def wrapper_validate_request_json(self, request, *args, **kwargs):
            try:
                if type == 0:
                    schema = {
                        "$schema": "http://json-schema.org/draft-07/schema#",
                        "$id": "http://example.com/product.schema.json",
                        "type": "object",
                        "properties": {
                            "api_details": {"type": "object"},
                            "api_parameters": {"type": "object"},
                        },
                        "required": ["api_details", "api_parameters"],
                        "additionalProperties": False,
                    }
                elif type == 1:
                    schema = {
                        "$schema": "http://json-schema.org/draft-07/schema#",
                        "$id": "http://example.com/product.schema.json",
                        "type": "object",
                        "properties": {
                            "api_details": {"type": "object"},
                            "session_details": {"type": "object"},
                            "api_parameters": {"type": "object"},
                        },
                        "required": ["api_details", "session_details", "api_parameters"],
                        "additionalProperties": False,
                    }
                import pdb
                pdb.set_trace()
                if request is not None and Draft7Validator(schema).is_valid(request.data):
                    return function(self, request, *args, **kwargs)
                else:
                    raise
            except Exception as err:
                return Response(status=400)
        return wrapper_validate_request_json
    return decorator_validate_request_json


def read_from_json_file(path):
    try:
        with open(path, 'r') as f:
            return {
                'status': 0,
                'message': f'Successfully json loaded from file {path}',
                'payload': json.load(f)
            }
        # return return_var
    except Exception:
        return {
            'status': 1,
            'message': f'Failed to load json from {path}',
        }
