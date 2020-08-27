# ---------------------- ALGORITHM ---------------------- #
# Step 1:   Check if emial exists in json with json schema validator
# Step 2:   If false, raise error and return Response 400, bad request.
#           If true get user from db, if not present send response email doesn't esist, create new account.
# Step 3:   If user is present return Response, user present, log in..
# ---------------------- End ---------------------- #
# ---------------------- Sample Request Body ---------------------- #
{
    "api_details": {
        "token_key": "",
        "development_key": ""
    },
    "api_parameters": {
        "user_name": "value",
    },
}
# ---------------------- End ---------------------- #
# ---------------------- Sample Response Body Success Case---------------------- #
{
    "api_payload": {
        "status": 0,        # 0 for success, 1 for failure
        "message": "Welcome user, log in to continue.",
    },
}
# ---------------------- End ---------------------- #
# ---------------------- Sample Response Body Failure Case---------------------- #
{
    "api_payload": {
        "status": 1,        # 0 for success, 1 for failure
        "message": "New User, sign up to continue.",
    },
}
# ---------------------- End ---------------------- #
