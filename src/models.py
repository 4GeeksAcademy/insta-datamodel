import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Following(Base):
    _tablename__ = 'Following'
username = Column(String(20), ForeignKey=True)
name = Column(String(250), nullable=False)
bio = Column(String(250))
email = Column(String(250))
phone_number = Column(Integer)

class Followers(Base):
    _tablename__ = 'Followers'
username = Column(String(20), ForeignKey=True)
name = Column(String(250), nullable=False)
bio = Column(String(250))
email = Column(String(250))
phone_number = Column(Integer)

class Story(Base):
    __tablename__ = "Story"
username = Column(String(20), ForeignKey=True)
caption = Column(String(250))
views = Column(Integer)
media_url = Column(String(250))

class Posts(Base):
    __tablename__ = 'Posts'
    user_id = Column(Integer, ForeignKey("username.id"))
    caption = Column(String(250))
    comments = Column(String(250))
    likes = Column(Integer)
    shares = Column(Integer)

class Username(Base):
    __tablename__ = 'Username'
    username = Column(String(20), nullable=False, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    phone_number = Column(Integer, nullable=False)
    posts = Column(Integer)
    bio = Column(String(250))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
