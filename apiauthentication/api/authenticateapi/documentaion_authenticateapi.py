# ---------------------- ALGORITHM ---------------------- #
# Step 1:   Check if requests exists in kwargs and
#           api_details exists in request.data and
#           if token_key and development_key exists in json with json schema validator
# Step 2:   If false, raise error and return Response 400, bad request.
#           If true get token string from db, if not present it'll raise error,
#           catch raised error and return Response 401, unauthorised.
# Step 3:   If key is present return function.
# ---------------------- End ---------------------- #
# ---------------------- Sample Request Body ---------------------- #
{
    "api_details": {
        "token_key": "",
        "development_key": ""
    },
    "api_parameters": {
        "key": "value"
    },
}
# ---------------------- End ---------------------- #
# ---------------------- Sample Response Body Success Case---------------------- #
{
    "session_payload": {
        "status": 0,        # 0 for success, 1 for failure
        "message": "",
        "payload": {
            "profile_id": 0,
            "session_id": 0,
            "session_key": ""
        }
    },
    "api_payload": {
        "status": 0,        # 0 for success, 1 for failure
        "message": "",
        "payload": {
            "key": "value"
        }
    },
}
# ---------------------- End ---------------------- #
# ---------------------- Sample Response Body Failure Case---------------------- #
# Response 400 or Response 401, no body
# ---------------------- End ---------------------- #
