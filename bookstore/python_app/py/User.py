#from Exceptions import *

class User:

    def __init__(self,username,password,email,address,phone,user_type):
        self.username = username
        self.password = password
        self.email = email
        self.address = address
        self.phone = phone
        self.user_type = user_type

    #return True if password is correct , else raise exception
    @staticmethod
    def is_password_correct(password):
        has_upper_case = False
        has_lower_case = False
        has_digit = False

        if len(password)< 0:
            raise IncorrectPasswordException()
        for index in password:
            if index.isupper():
                has_upper_case = True
            if index.islower():
                has_lower_case = True
            if index.isdigit():
                has_digit = True
        if has_upper_case == True and has_lower_case==True and has_digit==True and len(password) > 6:
            return True
        else:
            return False
            #raise IncorrectPasswordException()