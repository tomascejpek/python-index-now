class ErrorMessages:
    ERROR_202 = '202 Accepted - URL received. IndexNow key validation pending'
    ERROR_400 = '400 Bad request - Invalid format'
    ERROR_403 = '403 Forbidden - In case of key not valid (e.g. key not found, file found but key not in the file)'
    ERROR_422 = '422 Unprocessable Entity - In case of URLs which don’t belong to the host or the key is not matching the schema in the protocol'
    ERROR_429 = '429 Too Many Requests - Too Many Requests (potential Spam)'


class Exception202(Exception):
    pass


class Exception400(Exception):
    pass


class Exception403(Exception):
    pass


class Exception422(Exception):
    pass


class Exception429(Exception):
    pass
