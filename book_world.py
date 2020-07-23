class Author:
    def __init__(self,author_name,author_age,authors_nation):
        self.__author_name = author_name
        self.author_age = author_age
        self.authors_nation = authors_nation

    def get_author_name(self):
        return self.__author_name


class Book:
    def __init__(self,book_name,book_price,author_name,author_age,authors_nation):
        self.__book_name = book_name
        self.__book_price = book_price
        self.author_object = Author(author_name,author_age,authors_nation)

    def get_book_name(self):
        return self.__book_name

    def get_book_price(self):
        return self.__book_price

def total_price(book_objects):
    total_cost = 0
    for book_object in book_objects:
        total_cost+=book_object.get_book_price()
    return total_cost

def print_authors_books(book_objects,author_name):
    count=0
    for book_object in book_objects:
        if book_object.author_object.get_author_name().lower() == author_name.lower():
            count+=1
    return count

def affordable_books(book_objects):
    print("The affordable books are :")
    for book_object in book_objects:
        if book_object.get_book_price() < 1000:
            print(book_object.get_book_name(),":",book_object.author_object.get_author_name())
    
        
python_object = Book("Python",999,"Guido van rossum",64,"Dutch")
scala_object = Book("scala",1500,"Martin Odersky",61,"German")
java_object = Book("Java",800,"James Gosling",65,"Canadian")
c_object = Book("C",1999,"Dennis Ritche",79,"American")
c_plus_object = Book("C++",1499,"Bjarne Stroustrup",69,"Danish")
generic_java_object = Book("Generic Java",599,"Martin Odersky",61,"German")

book_objects =[python_object,scala_object,java_object,c_object,c_plus_object,generic_java_object]
print("The total price of the books is",total_price(book_objects))
author_name = input("Enter the author name to calculate total number of books :")
print("The total number books written by",author_name,"is",print_authors_books(book_objects,author_name),"\n")
affordable_books(book_objects)

"""
Input and Output:
The total price of the books is 7396
Enter the author name to calculate total number of books :martin odersky
The total number books written by martin odersky is 2 

The affordable books are :
Python : Guido van rossum
Java : James Gosling
Generic Java : Martin Odersky
"""
