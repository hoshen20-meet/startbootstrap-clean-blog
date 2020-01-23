from sqlalchemy import Column, Integer , String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()


class article(Base):
   __tablename__ = 'article'
   article_id = Column(Integer, primary_key=True)
   title = Column(String)
   paragraph = Column(String)
   release_date = Column(String)
   author = Column(String)
   

class Books(Base):
    __tablename__ = 'Books'
    Book_id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Integer)
    authorname=Column(String)
    pic= Column(String)
   
def hash_password(self, password):
	  self.password_hash = pwd_security.encrypt(password)
def verify_password(self, password):
   return pwd_security.verify(password,self.password_hash)
