from chalice import BadRequestError, Response


def handle_error(e: Exception):

    if isinstance(e, BadRequestError):
        return Response(status_code=400, body={'status': 'failed', 'message': str(e)})

    return Response(status_code=400, body={'status': 'failed', 'message': str(e)})
