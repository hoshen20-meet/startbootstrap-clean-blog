from model import *
from sqlalchemy.pool import SingletonThreadPool

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(title,paragraph,release_date,author):
        article_object = article(
        title = title,
        paragraph = paragraph,
        release_date = release_date,
        author = author)
        session.add(article_object)
        session.commit()

def query_article_by_name(name):
	"""
	Find the first student in the database,
	by their name
	"""
	Article = session.query(article).filter_by(
		name=name).first()
	return Customer

def query_all_article():
	"""
	Print all the students in the database.
	"""
	Article = session.query(article).all()
	return article

def delete_article_id(id_number):
	"""
	Delete all students with a certain name
	from the database.
	"""
	session.query(article).filter_by(
		article_id=id_number).delete()
	session.commit()

def delete_article_name(name):
	"""
	Delete all students with a certain name
	from the database.
	"""
	session.query(article).filter_by(
		name=name).delete()
	session.commit()

##def update_lab_status(name, finished_lab):
##	"""
##	Update a student in the database, with 
##	whether or not they have finished the lab
##	"""
##	Customer_object = session.query(Customers).filter_by(
##		name=name).first()
##	Customer_object.finished_lab = finished_lab
##	session.commit()

def query_article_by_id(article_id):
    Article = session.query(article).filter_by(
            article_id=article).first()
    return article


def hash_password(self, password):
        self.password_hash = pwd_security.encrypt(password)
def verify_password(self, password):
        return pwd_security.verify(password,self.password_hash)



def add_book(name, author, price, img):
	"""
	Add a student to the database, given
	their name, year, and whether they have
	finished the lab.
	"""
	Book_object = Books(title=name, price=price, authorname=author, pic=img)
	session.add(Book_object)
	session.commit()

def query_book_by_name(name):
	"""
	Find the first student in the database,
	by their name
	"""
	Books = session.query(Books).filter_by(
		name=name).first()
	return Books

def query_all_books():
	"""
	Print all the students in the database.
	"""
	books = session.query(Books).all()
	return books

def delete_book_id(id_number):
	"""
	Delete all students with a certain name
	from the database.
	"""
	session.query(Books).filter_by(
		Book_id=id_number).delete()
	session.commit()

def delete_book_name(name):
	"""
	Delete all students with a certain name
	from the database.
	"""
	session.query(Books).filter_by(
		name=name).delete()
	session.commit()

##def update_lab_status(name, finished_lab):
##	"""
##	Update a student in the database, with 
##	whether or not they have finished the lab
##	"""
##	Customer_object = session.query(Customers).filter_by(
##		name=name).first()
##	Customer_object.finished_lab = finished_lab
##	session.commit()

def query_book_by_id(Book_id):
    Books = session.query(Books).filter_by(
            Book_id=Book_id).first()
    return student



