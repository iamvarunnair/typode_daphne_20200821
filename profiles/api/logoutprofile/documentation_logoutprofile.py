# ---------------------- ALGORITHM ---------------------- #
# Step 1:   check if session exists and is active.
#           If not, send Response with status 403 forbidden
#           If it does, update session key and status to 2(inactive)
# ---------------------- End ---------------------- #
# ---------------------- Sample Request Body ---------------------- #
{
    "api_details": {
        "token_key": "",
        "development_key": ""
    },
    "session_details": {
        "profile_id": 0,
        "session_id": 0,
        "session_key": ""
    },
    "api_parameters": {},
}
# ---------------------- End ---------------------- #
# ---------------------- Sample Response Body Success Case---------------------- #
{
    "api_payload": {
        "status": 0,        # 0 for success, 1 for failure
        "message": "Successfully logged out.",
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
