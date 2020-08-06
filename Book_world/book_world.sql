create table book(
	bookid serial primary key,
	bookname text not null,
	bookprice numeric not null
						 
);
insert into book(bookname,bookprice) values('c',1200)					
select * from book