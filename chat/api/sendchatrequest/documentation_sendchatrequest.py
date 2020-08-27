# ---------------------- ALGORITHM ---------------------- #
# Friend request statuses
#
# 1 request sent
# 2 request accepted
# 3 request rejected
# 4 request withdrawn
# 5 removed (from contacts)
#
# Step 1:   Check if correct keys exist in api_parameters json with json schema validator
# Step 2:   If false, raise error and return Response 400, bad request.
#           If true check chat request exist with status 1(request sent) or 2(request accepted).
# Step 3:   If present, send status 1(failure), request already exists.
#           if not present serialize and enter request in db.
# Step 4:   Return session and status 0(success) response status 200.
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
    "api_parameters": {
        "send_to": 0,
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
        "message": "Successfully sent request.",
    },
}
# ---------------------- End ---------------------- #
# ---------------------- Sample Response Body Failure Case---------------------- #
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
        "status": 1,        # 0 for success, 1 for failure
        "message": "Failed to send request.",
    },
}
# ---------------------- End ---------------------- #
