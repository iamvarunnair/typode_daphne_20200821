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
#           If true fetch chat request with
#           ((requester_id = session profile_id and responder_id = api_parameter profile_id)
#           or (requester_id = session profile_id and responder_id = api_parameter profile_id))
#           and status 2(request accepted).
# Step 3:   If not present, send status 1(failure), contact doesn't exist.
#           if present update request status to 5(removed) value in db.
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
        "profile_id": 0,
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
        "message": "Successfully removed contact.",
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
        "message": "Failed to remove contact.",
    },
}
# ---------------------- End ---------------------- #
