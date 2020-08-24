# ---------------------- ALGORITHM ---------------------- #
# Step 1:   Check if requests exists in kwargs and
#           session_details exists in request.data and
#           if profile_id, session_id and session_key exists in json with json schema validator
# Step 2:   If false, raise error and return Response 400, bad request.
#           If true fetch and select for update (to lock db row inside atomic transaction) from db,
#           and update session_key, if not present update status of session with session_id to 2(Inactive).
# Step 3:   If update is successful, return function with session_payload(updated sessions) in request.data as success.
# ---------------------- End ---------------------- #
# ---------------------- Sample Request Body ---------------------- #
{
    "session_details": {
        "profile_id": 0,
        "session_id": 0,
        "session_key": "",
    },
}
# ---------------------- End ---------------------- #
# ---------------------- Sample Response Body Success Case---------------------- #
{
    "session_payload": {
        "status": 0,        # 0 for success, 1 for failure
        "message": "Successfully updated session.",
        "payload": {
            "profile_id": 0,
            "session_id": 0,
            "session_key": ""
        }
    },
}
# ---------------------- End ---------------------- #
# ---------------------- Sample Response Body Failure Case---------------------- #
{
    "session_payload": {
        "status": 1,        # 0 for success, 1 for failure
        "message": "Failed to update sessions.",
    },
}
# ---------------------- End ---------------------- #
