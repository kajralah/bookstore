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

    def book_title(self):
        return self.__book_title

    def book_price(self):
        return self.__book_price

    def book_author(self):
        return self.__book_author
    
    def book_pages(self):
        return self.__book_pages

    def book_publisher(self):
        return self.__book_publisher

    def book_description(self):
        return self.__book_description

    def book_category(self):
        return self.__book_category

    def book_image(self):
        return self.__book_image    
