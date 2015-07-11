import cx_Oracle
from bookstore.python_app.py.User import *
from bookstore.python_app.py.Exceptions import *
from bookstore.python_app.py.Book import *
from bookstore.python_app.py.DBQueries import *
import datetime
from django.core.mail import send_mail


class DBController:

    def __init__(self):
        self.con = None

    # connecting to the database with 
    # the given DB_connection parameters
    def __connect_to_db(self):
        con = cx_Oracle.connect(DB_connection)
        return con

    # throws ExistingUserException()
    # adding User in Db or throw exception
    def add_user_to_db(self, username, password, email, address, phone):
        if self.return_existing_user(username, password) is None:
            db_connection = self.__connect_to_db()
            cur = db_connection.cursor()
            cur.execute(INSERT_USER_TO_DB, uname=username, upass=password,
                        uemail=email, uaddress=address,
                        uphone=phone, usupervisor='F')
            db_connection.commit()
            cur.close()
            db_connection.close()
        else:
            raise ExistingUserException()

    # returns user_id if we have result from the query
    # returns None otherwise
    def get_user_id(self, username, password):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(GET_USER_ID, username=username, password=password)
        db_connection.commit()
        for result in cur:
            if result[0] is None:
                return None
            else:
                return result[0]
        cur.close()
        db_connection.close()

    # returns new User if we have user with this id
    # returns None otherwise
    def return_user_by_id(self, id):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(GET_USER_FROM_ID, id=id)
        db_connection.commit()
        for result in cur:
            if result[1] is not None:
                user = User(result[1], result[2], result[3],
                            result[4], result[5], result[6])
                cur.close()
                db_connection.close()
                return user
            else:
                cur.close()
                db_connection.close()
                return None

    # returns new User if there is user with this username and password
    # return None otherwise
    def return_existing_user(self, username, password):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(FIND_USER_IN_DB, uname=username, upass=password)
        db_connection.commit()
        for result in cur:
            if result[1] is not None:
                user = User(result[1], result[2], result[3],
                            result[4], result[5], result[6])
                cur.close()
                db_connection.close()
                return user
            else:
                cur.close()
                db_connection.close()
                return None

    # returns True if user is changed
    def change_user(self, user_id, password, email, address, phone):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(CHANGE_USER, uemail=email, uphone=phone,
                    uaddress=address, upass=password, user_id=user_id)
        db_connection.commit()
        cur.close()
        db_connection.close()
        return True

    # return True if we added the book in the database
    def add_book_to_db(self, book_title, book_price, book_author,
                       book_pages, book_image, book_publisher,
                       book_description, category_id):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(ADD_BOOK, btitle=book_title,
                    bprice=book_price, bauthor=book_author,
                    bpages=book_pages, bpublish=book_description,
                    bdesc=book_description,
                    bimg=book_image, bcategory=category_id)
        db_connection.commit()
        cur.close()
        db_connection.close()
        return True

    # returns the category_id for the given category_name
    def get_category_id_by_name(self, category_name):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(GET_CATEGORIES_BY_NAME, category_name=category_name)
        db_connection.commit()
        category_id = 0
        for result in cur:
            category_id = result[0]
        cur.close()
        db_connection.close()
        return category_id

    # returns the number of liked product for the user with this user_id
    def number_of_liked_product(self, user_id):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(GET_USER_LIKED_INFO, id=user_id)
        db_connection.commit()
        number_of_liked_products = 0
        for result in cur:
            number_of_liked_products += 1
        cur.close()
        db_connection.close()
        return number_of_liked_products

    # returns the number of bought items for the user with this user_id
    def number_of_bought_items(self, user_id):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(GET_USER_BOUGHT_INFO, id=user_id)
        db_connection.commit()
        number_of_bought_item = 0
        for result in cur:
            number_of_bought_item += 1
        cur.close()
        db_connection.close()
        return number_of_bought_item

    # getting tuple of all categories for showing them in the menu
    def get_categories(self):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(GET_CATEGORIES)
        db_connection.commit()
        list_of_categories = ()
        list_of_categories = list(list_of_categories)
        for result in cur:
            list_of_categories.append(result)
        cur.close()
        db_connection.close()
        return tuple(list_of_categories)

    # getting information for all available books in the database
    # for showing them in the main page
    # returns list of the books
    def show_book(self):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(GET_BOOK_FOR_SHOW)
        db_connection.commit()
        list_of_book = []
        for result in cur:
            list_of_book.append(result)
            list_of_book.append(",")
        cur.close()
        db_connection.close()
        return list_of_book

    # getting the book_id by given book title
    def get_book_id_by_title(self, title):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(GET_BOOK_ID_BY_NAME, book_title=title)
        db_connection.commit()
        book_id = 0
        for result in cur:
            book_id = result[0]
        cur.close()
        db_connection.close()
        return book_id

    # getting the book information from book id
    # returns new Book with that id
    def get_book_by_id(self, id):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(GET_BOOK_BY_ID, book_id=id)
        db_connection.commit()
        for result in cur:
            book = Book(result[1], result[2], result[3], result[
                        4], result[5], result[6], result[7], result[8])
        cur.close()
        db_connection.close()
        return book

    # getting the category name by the category id
    # returns category name
    def get_categorie_by_id(self, id):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(GET_CATEGORIE_NAME_BY_ID, category_id=id)
        db_connection.commit()
        for result in cur:
            category_name = result[0]
        cur.close()
        db_connection.close()
        return category_name

    # Returns False if the user doesn't like yet this category
    # returns the category_id otherwise
    def check_for_liked_categories(self, user_id, category_name):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        category_id = db.get_category_id_by_name(category_name)
        cur.execute(LIKED_CATEGORIES, user_id=user_id, category_id=category_id)
        db_connection.commit()
        has_category = ""
        for result in cur:
            has_category = result[0]
        cur.close()
        db_connection.close()
        if has_category is "":
            return False
        else:
            return has_category

    # return true if category is added in user_liked_category
    # return false if user already liked this category
    def insert_into_liked_categories(self, user_id, category_name):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        category_id = db.get_category_id_by_name(category_name)
        if self.check_for_liked_categories(user_id, category_name) is False:
            cur.execute(INSERT_LIKED_CATEGORY, user_id=user_id,
                        category_id=category_id, want_email='T')
            db_connection.commit()
            cur.close()
            db_connection.close()

    # adding book id in the user_liked_books and adding the category
    # if the user haven't liked this category yet
    # return False if we can't add the book
    def insert_into_user_liked_books(self, user_id, book_title, category_name):
        result = ''
        try:
            db_connection = self.__connect_to_db()
            cur = db_connection.cursor()
            db.insert_into_liked_categories(user_id, category_name)
            book_id = self.get_book_id_by_title(book_title)
            cur.execute(INSERT_LIKED_BOOKS, user_id=user_id, book_id=book_id)
            db_connection.commit()
            result = True
            return result
        except Exception as e:
            result = False
            return result
        finally:
            cur.close()
            db_connection.close()

    # adding book_id in the user bought information
    # returns True if it is added
    def insert_into_user_bought(self, user_id, book_title):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        book_id = self.get_book_id_by_title(book_title)
        date = datetime.date.today().strftime("%d-%B-%Y")
        cur.execute(INSERT_BOUGHT_BOOKS, user_id=user_id, book_id=book_id)
        db_connection.commit()
        cur.close()
        db_connection.close()
        return True

    # return True if this user with this user_id is supervisor
    # retun False otherwise
    def is_supervisor(self, user_id):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(IS_SUPERVISOR, user_id=user_id)
        db_connection.commit()
        for result in cur:
            if result[0] is 'T':
                is_supervisor = True
            else:
                is_supervisor = False
        cur.close()
        db_connection.close()
        return is_supervisor

    # getting bought books for current user with this user_id
    # return list of bought books by this user
    def show_bought_books_by_user(self, user_id):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(GET_USERS_BOUGHT_BOOKS, user_id=user_id)
        db_connection.commit()
        list_of_book = []
        for result in cur:
            lst = list(result)
            lst[9] = lst[9].strftime("%Y-%m-%d %H:%M:%S")
            result_book = tuple(lst)
            list_of_book.append(result_book)
            list_of_book.append(",")
        cur.close()
        db_connection.close()
        return list_of_book

    # updating information about user wants or not to receive email
    # returns True if update is done
    def update_sending_email(self, user_id, wants_email):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(
            UPDATE_USER_WANT_EMAIL, wants_email=wants_email, user_id=user_id)
        db_connection.commit()
        cur.close()
        db_connection.close()
        return True

    # getting all emails from the users that like the
    # category with this category id
    # returns list of the emails
    def get_emails_for_sending_msg(self, category_id):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(
            GET_USER_EMAILS_FOR_SENDING_MESSAGE, category_id=category_id)
        db_connection.commit()
        list_of_emails = []
        for result in cur:
            list_of_emails.extend(result)
        cur.close()
        db_connection.close()
        return list_of_emails

    # sending email to all users that like this category
    # and want to receive emails
    # don't return anything
    def send_emails(self, the_message, category_id):
        import smtplib
        gmail_user = "bookstorebulgaria@gmail.com"
        gmail_pwd = "thebookstore"
        FROM = 'Bookstore'
        TO = self.get_emails_for_sending_msg(category_id)
        SUBJECT = "Bookstore - new book"
        TEXT = the_message

        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            for email in TO:
                server.sendmail(FROM, email, message)
            server.close()
        except:
            pass

    # getting books from certain category
    # with this category name
    # returns list of the books
    def show_books_for_category(self, category_name):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        cur.execute(GET_BOOK_FOR_SHOW_FROM_CATEGORY,
                    category_id=self.get_category_id_by_name(category_name))
        db_connection.commit()
        list_of_book = []
        for result in cur:
            list_of_book.append(result)
            list_of_book.append(",")
        cur.close()
        db_connection.close()
        return list_of_book

    # getting information about what is been searched for
    # returns list of books which title is like the seached word
    def show_search_book(self, searched_book):
        db_connection = self.__connect_to_db()
        cur = db_connection.cursor()
        search_book = '%'+searched_book+'%'
        cur.execute(GET_BOOK_FROM_SEARCH, book_title=search_book)
        db_connection.commit()
        list_of_book = []
        for result in cur:
            list_of_book.append(result)
            list_of_book.append(",")
        cur.close()
        db_connection.close()
        return list_of_book
