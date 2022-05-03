def abort(status_code: int):
    status_list = {
        200: "OK",
        302: "Found",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
    }
    return {
        "status_code": status_code,
        "status":status_list[status_code]
        }
