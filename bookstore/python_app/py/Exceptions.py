class IncorrectPasswordException(BaseException):
    def __init__(self):
        print('Incorrect password')

class ExistingUserException(BaseException):
    def __init__(self):
        print('Existing User')

class InvalidBookException(BaseException):
    def __init__(self):
        print('Invalid Book')

class InvalidUserException(BaseException):
    def __init__(self):
        print('Invalid User')