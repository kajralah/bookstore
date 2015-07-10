from bookstore.python_app.py.Exceptions import *
from bookstore.python_app.py.DBController import *


class User:

    def __init__(self, username, password,
                 email, address, phone, is_supervisor):
        self.__username = username
        self.__password = password
        self.__email = email
        self.__address = address
        self.__phone = phone
        self.__is_supervisor = is_supervisor

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def email(self):
        return self.__email

    @property
    def address(self):
        return self.__address

    @property
    def phone(self):
        return self.__phone

    @property
    def is_supervisor(self):
        return self.__is_supervisor

    # return True if password is correct , else raise exception
    @staticmethod
    def is_password_correct(password):
        has_upper_case = False
        has_lower_case = False
        has_digit = False

        if len(password) < 0:
            raise IncorrectPasswordException()
        for index in password:
            if index.isupper():
                has_upper_case = True
            if index.islower():
                has_lower_case = True
            if index.isdigit():
                has_digit = True
        if has_upper_case is True and has_lower_case is True
        and has_digit is True and len(password) > 6:
            return True
        else:
            return False
