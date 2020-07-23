class BookWorld:
    def __init__(self,books_dict):
        self.books_dict = books_dict
        self.affordable_list = []
    
    def calculate_total_price(self):
        total = 0
        for book,price in self.books_dict.items():
            total = total + price
        return total

    def affordable_books(self):
        for book,price in self.books_dict.items():
            if price < 1000:
                self.affordable_list.append(book)
        return self.affordable_list
        
class Book:
    def __init__(self,book_name,author_name,author_age,authors_nation):
        self.book_name = book_name
        self.author_name = author_name
        self.author_age = author_age
        self.authors_nation = authors_nation

    def get_author_name(self):
        return self.author_name

    def get_book_name(self):
        return self.book_name

def display_affordable_books(book_objects):
    print("The affordable books :\nBook     Author\n")
    affordable_list = book_world.affordable_books()
    for book_object in book_objects:
        if book_object.get_book_name() in affordable_list:
            print(book_object.get_book_name(),":",book_object.get_author_name())

def number_of_books_of_author(book_objects,author_name):
    count =0
    for book_object in book_objects:
        if book_object.get_author_name().lower() == author_name.lower():
            count+=1
    return count

book_world = BookWorld({"Python" : 999,"Scala" : 1500,"Java" : 800,"C" : 1999,"C++" : 1499,"Generic Java" : 599})

python_object = Book("Python","Guido van rossum",64,"Dutch")
scala_object = Book("scala","Martin Odersky",61,"German")
java_object = Book("Java","James Gosling",65,"Canadian")
c_object = Book("C","Dennis Ritche",79,"American")
c_plus_object = Book("C++","Bjarne Stroustrup",69,"Danish")
generic_java_object = Book("Generic Java","Martin Odersky",61,"German")

book_objects =[python_object,scala_object,java_object,c_object,c_plus_object,generic_java_object]

print("The price of all the books in the store is",book_world.calculate_total_price())

author_name = input("Enter the author name to calculate total number of books :")
print("The total number books written by",author_name,"is",number_of_books_of_author(book_objects,author_name),"\n")

display_affordable_books(book_objects)


"""
Input and Output :

The price of all the books in the store is 7396
Enter the author name to calculate total number of books :martin odersky
The total number books written by martin odersky is 2 

The affordable books :
Book     Author

Python : Guido van rossum
Java : James Gosling
Generic Java : Martin Odersky

"""
