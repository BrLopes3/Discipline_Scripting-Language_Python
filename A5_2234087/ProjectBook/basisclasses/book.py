"""
Assignmet 5
Student: Bruno Lopes
Date: 2023-11-11

3) Create the class Book with the following characteristics:

"""

class Book:

    # Class attribute
    __bookId = 0

    # Constructor
    def __init__(self, bookTitle, bookAuthor, bookEditor, bookPrice):
        Book.__bookId += 1
        self.__bookId = Book.__bookId
        self.__bookTitle = bookTitle
        self.__bookAuthor = bookAuthor
        self.__bookEditor = bookEditor
        self.__bookPrice = bookPrice

    # Getters and Setters
    def getBookId(self):
        return self.__bookId

    def getBookTitle(self):
        return self.__bookTitle

    def getBookAuthor(self):
        return self.__bookAuthor

    def getBookEditor(self):
        return self.__bookEditor

    def getBookPrice(self):
        return self.__bookPrice

    ## set only the price 
    def setBookPrice(self, bookPrice):
        self.__bookPrice = bookPrice

    def __str__(self):
        return f"Book ID: {self.__bookId}, Book Name: {self.__bookTitle}, Author Name: {self.__bookAuthor}, Price: {self.__bookPrice}"

