class APIException(Exception):
    status_code = 500
    message = 'Something went wrong'

    def __init__(self, message=None, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        if message is not None:
            self.message = message

        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class ResourceExists(APIException):
    status_code = 409
    message = 'Resource already exists'


class InvalidInputData(APIException):
    status_code = 400
    message = 'Input data are malformed'
