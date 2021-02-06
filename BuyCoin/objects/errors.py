class Error(BaseException):
    pass


class QueryError(Error):
    def __init__(self, message=None, status=None):
        self.message = message
        self.status = status if status else 400

    @property
    def response(self):
        return {"message": self.message, "status_code": self.status}


class ClientError(Error):
    def __init__(self, message=None, status=None):
        self.message = message
        self.status = status if status else 401

    @property
    def response(self):
        return {"message": self.message, "status_code": self.status}


class InvalidInstance(Error):
    '''
    InvalidInstance class
    '''
    message = 'Not a valid instance of type : '
    manager = ''

    def __init__(self, manager):
        self.manager = manager

    def __str__(self):
        return '%s %s' % (self.message, self.manager)
