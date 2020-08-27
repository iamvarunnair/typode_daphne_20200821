# ---------------------- ALGORITHM ---------------------- #
# Step 1:   Check user_name and password  exists in json with json schema validator
# Step 2:   If false, raise error and return Response 400, bad request.
#           If true check user presence in db.
# Step 3:   If present, send status 1(failure), user already exists.
#           if not present serialize and enter profile in d.
# Step 4:   Log user in.
# Step 4:   Return session and status 0(success) response status 200.
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
        "avatar_id": 0
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
        "message": "Successfully created profile and logged in.",
    },
}
# ---------------------- End ---------------------- #
# ---------------------- Sample Response Body Failure Case---------------------- #
{
    "api_payload": {
        "status": 1,        # 0 for success, 1 for failure
        "message": "Failed to create profile, it already exists.",
    },
}
# ---------------------- End ---------------------- #
