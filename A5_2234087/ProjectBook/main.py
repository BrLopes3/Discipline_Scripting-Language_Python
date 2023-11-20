"""
Assignment 5
Student: Bruno Lopes
Date: 2023-11-11

"""
from basisclasses.book import Book

if __name__ == '__main__':

    book1 = Book('The Shining', 'Stephen King', 'Editor1', 20.50)
    print(book1.__str__())

    book2 = Book('Carrie', 'Stephen King', 'Editor1', 20.51)
    print(book2.__str__())

    book3 = Book('Doctor Sleep', 'Stephen King', 'Editor1', 20.52)
    print(book3.__str__())

    book4 = Book('Under the Dome', 'Stephen King', 'Editor1', 20.53)
    print(book4.__str__())

    book5 = Book('The Dark Tower', 'Stephen King', 'Editor1', 20.47)
    print(book5.__str__()) 

