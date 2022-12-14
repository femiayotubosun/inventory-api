def generic_success_response(message="success", result=None, status_code=200):
    return {
        "result": result,
        "status_code": status_code,
        "message": message,
        "status": "success",
    }


def generic_failure_response(message="success", result=None, status_code=400):
    return {
        "result": result,
        "status_code": status_code,
        "eorr": message,
        "status": "failure",
    }


def create_resource_success_response(
    message="resource created", result=None, status_code=201
):
    return generic_success_response(message, result, status_code)


def delete_resource_success_response(
    message="resource deleted", result=None, status_code=204
):
    return generic_success_response(message, result, status_code)
