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
        "user_name": "value",
        "password": "value",
    },
}
# ---------------------- End ---------------------- #
# ---------------------- Sample Response Body Success Case---------------------- #
{
    "session_payload": {
        "status": 0,        # 0 for success, 1 for failure
        "message": "Successfully session genarated.",
        "payload": {
            "profile_id": 0,
            "session_id": 0,
            "session_key": ""
        }
    },
    "api_payload": {
        "status": 0,        # 0 for success, 1 for failure
        "message": "Successfully logged in.",
    },
}
# ---------------------- End ---------------------- #
# ---------------------- Sample Response Body Failure Case---------------------- #
{
    "api_payload": {
        "status": 1,        # 0 for success, 1 for failure
        "message": "Failed to log in.",
    },
}
# ---------------------- End ---------------------- #
