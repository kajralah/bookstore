import cx_Oracle
from bookstore.python_app.py.User import *
from bookstore.python_app.py.Exceptions import *
from bookstore.python_app.py.Book import *


DB_name = 'HR'
DB_password = 'HR'
DB_host = 'localhost'
DB_connection = DB_name + '/' + DB_password + '@' + DB_host
INSERT_USER_TO_DB = 'INSERT INTO USERS(USERNAME,USER_PASSWORD,USER_EMAIL,USER_ADDRESS,USER_PHONE,USER_TYPE) VALUES (:uname,:upass,:uemail,:uaddress,:uphone,:utype)'
FIND_USER_IN_DB = 'SELECT* FROM USERS WHERE USERNAME= :uname AND USER_PASSWORD= :upass'
CHANGE_USER = 'UPDATE USERS SET USER_EMAIL =:uemail,USER_PHONE=:uphone,USER_ADDRESS=:uaddress,USER_PASSWORD=:upass WHERE USERNAME =:uname'
ADD_BOOK = 'INSERT INTO BOOK(BOOK_TITLE,BOOK_PRICE,BOOK_AUTHOR,BOOK_PAGES,BOOK_PUBLISHER,BOOK_DESCRIPTION,CATEGORY_ID VALUES(:btitle,:bprice,:bauthor,:bpages,:bpublish,:bdesc,:bcategory)'
GET_BOOK_FROM_DB = 'SELECT * FROM BOOK WHERE CATEGORY_ID=:category_id'
GET_USER_ID = 'SELECT USER_ID FROM USERS WHERE USERNAME =:username AND USER_PASSWORD =:password'
GET_USER_FROM_ID = 'SELECT * FROM USERS WHERE USER_ID=:id'
GET_USER_LIKED_INFO = 'SELECT * FROM USER_LIKED_CATEGORIES WHERE USER_ID=:id'
GET_USER_BOUGHT_INFO = 'SELECT * FROM USER_BOUGHT WHERE USER_ID = :id'

class DBController:

    def __init__(self):
        self.con = None

    def __connect_to_db(self):
        con = cx_Oracle.connect(DB_connection)
        return con

    # throws existingUserException() and cx_Oracle.IntegrityError
    # adding User in Db or throw exception
    def add_user_to_db(self, username, password, email, address, phone, user_type):
        if self.return_existing_user(username, password) is None:
            db_connection = self.__connect_to_db()
            cur = db_connection.cursor()
            cur.execute(INSERT_USER_TO_DB, uname=username, upass=password,
                        uemail=email, uaddress=address, uphone=phone, utype=user_type)
            db_connection.commit()
            cur.close()
            db_connection.close()
        else:
            raise ExistingUserException()

    def get_user_id(self,username,password):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(GET_USER_ID,username= username,password=password)
        db_connection.commit()
        for result in cur:
            if result[0] is None:
                return None
            else:
                return result[0]
        cur.close()
        db_connection.close()

    def return_user_by_id(self,id):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(GET_USER_FROM_ID,id=id)
        db_connection.commit()
        for result in cur:
            if result[1] is not None:
                user = User(result[1], result[2], result[3], result[4], result[5], result[6])
                cur.close()
                db_connection.close()
                return user
            else:
                cur.close()
                db_connection.close()
                return None

    # return None if there is not such user or returns the User if there is
    # such user
    def return_existing_user(self, username, password):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(FIND_USER_IN_DB, uname=username, upass=password)
        db_connection.commit()
        for result in cur:
            if result[1] is not None:
                user = User(result[1], result[2], result[3], result[4], result[5], result[6])
                cur.close()
                db_connection.close()
                return user
            else:
                cur.close()
                db_connection.close()
                return None

    # the password is checked and the existing of the user is checked before invoking this function
    # returns True if user is changed else raise cx_ORacle.IntegrityError
    # cannot change the type of the user
    def change_user(self, username, password, email, address, phone):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(CHANGE_USER, uemail=email, uphone=phone,
                    uaddress=address, upass=password, uname=username)
        db_connection.commit()
        cur.close()
        db_connection.close()
        return True

    # add blob picture?
    # return True if added else raise cx_oracle integrity error
    def add_book_to_db(self, book_title, book_price, book_author, book_pages, book_publisher, book_description, category_id):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(ADD_BOOK, btitle=book_title, bprice=book_price, bauthor=book_author,
                    bpages=book_pages, bpublish=book_description, bdesc=book_description, bcategory=category_id)
        db_connection.commit()
        cur.close()
        db_connection.close()
        return True

    # read the image!!
    def get_book_from_db(self, category_id):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(GET_BOOK_FROM_DB, category_id=category_id)
        db_connection.commit()
        for result in cur:
            book = Book(
                result[1], result[2], result[3], result[4], result[5], result[6], result[7])
        db_connection.close()
        cur.close()
        return book
    # read certain book

    # add record to user liked

    def number_of_liked_product(self,user_id):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(GET_USER_LIKED_INFO,id =user_id)
        db_connection.commit()
        number_of_liked_products = 0
        for result in cur:
            number_of_liked_products += 1
        cur.close()
        db_connection.close()
        return number_of_liked_products

    def number_of_bought_items(self,user_id):
        db_connection=self.__connect_to_db()
        cur= db_connection.cursor()
        cur.execute(GET_USER_BOUGHT_INFO,id=user_id)   
        db_connection.commit()
        number_of_bought_item = 0
        for result in cur:
            number_of_bought_item += 1
        cur.close()
        db_connection.close()
        return number_of_bought_item