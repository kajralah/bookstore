from bookstore.python_app.py.Exceptions import *

class Book:

    #add book-img blob ? 
    def __init__(self,book_title,book_price,book_author,book_pages,book_publisher,book_description,book_category):
        this.book_title = book_title
        this.book_price = book_price
        this.book_author = book_author
        this.book_pages = book_pages
        this.book_publisher = book_publisher
        this.book_description = book_description
        this.book_category = book_category

    @staticmethod
    def validating_book(self,book_title,book_price,book_author,book_pages,book_publisher,book_description,book_category):
        if book_title is not None and book_price is not None and book_author is not None and book_pages is not None and book_publisher is not None:
            return True
        else:
            raise InvalidBookException()
