from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class BookWorld(Base):
    __tablename__ = 'book'
    bookid = Column(Integer,primary_key=True)
    bookname = Column(String(120))
    bookprice = Column(Integer)

