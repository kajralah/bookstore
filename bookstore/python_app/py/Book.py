#from bookstore.python_app.py.Exceptions import *

class Book:

    def __init__(self,book_title,book_price,book_author,book_pages,book_publisher,book_description,book_category,book_image):
        self.__book_title = book_title
        self.__book_price = book_price
        self.__book_author = book_author
        self.__book_pages = book_pages
        self.__book_publisher = book_publisher
        self.__book_description = book_description
        self.__book_category = book_category
        self.__book_image = book_image

    @staticmethod
    def validating_book(self,book_title,book_price,book_author,book_pages,book_publisher,book_description,book_category):
        if book_title is not None and book_price is not None and book_author is not None and book_pages is not None and book_publisher is not None:
            return True
        else:
            raise InvalidBookException()

    @property
    def book_title(self):
        return self.__book_title

    @property
    def book_price(self):
        return self.__book_price

    @property
    def book_author(self):
        return self.__book_author
    
    @property
    def book_pages(self):
        return self.__book_pages

    @property
    def book_publisher(self):
        return self.__book_publisher

    @property
    def book_description(self):
        return self.__book_description

    @property
    def book_category(self):
        return self.__book_category

    @property
    def book_image(self):
        return self.__book_image    
