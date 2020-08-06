from flask import Flask, request,jsonify
from sqlalchemy import create_engine
from book_world import BookWorld
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['DEBUG']= True

def connect_db():
    connection_string = "postgresql://postgres:Sathya@12@localhost:5432/BookWorld"
    return create_engine(connection_string)

def format_list(row):
    return "name: "+str(row.bookname)+" "+"price: "+str(row.bookprice)
@app.route('/',methods=['GET'])
def get_books():
    book_list=session.query(BookWorld).all()
    book = [format_list(row) for row in book_list]
    return jsonify(book)

@app.route('/insert',methods=['POST'])
def insert_book():
    book_name = request.form['bookname']
    book_price = request.form['bookprice']
    obj = BookWorld(bookname=book_name,bookprice=book_price)
    session.add(obj)
    session.commit()
    return "Data added successfully"

@app.route('/update',methods=['PUT'])
def update_book():
    book_name = request.form['bookname']
    book_price = request.form['bookprice']
    updated_book = session.query(BookWorld).filter_by(bookname= book_name).one()
    updated_book.bookname = book_name
    updated_book.bookprice = book_price
    session.add(updated_book)
    session.commit()
    return "Data updated successfully"

@app.route('/delete',methods=['DELETE'])
def delete_book():
    book_name = request.form['bookname']
    delete_book = session.query(BookWorld).filter_by(bookname=book_name).one()
    session.delete(delete_book)
    session.commit()
    return "Book deleted successfully"




db = connect_db()
Session = sessionmaker(bind=db)
session = Session()
print("Database connected successfully")
if __name__ == "__main__":
    app.run(debug=True)




