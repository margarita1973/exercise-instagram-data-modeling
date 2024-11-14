import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, PrimaryKeyConstraint
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,  primary_key=True)
    user_name = Column(String, unique=True, nullable=False)
    firstname = Column(String(30))
    lastname = Column (String(30))
    email = Column (String(40), unique=True, nullable=False)
    comments = relationship ('Comment', back_populates="author_relationship")
    likes = relationship('Likes', back_populates='user_rel')
    follows = relationship('Follow', back_populates ='user_rel')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    post_text =Column(String (300))
    user_id = Column(Integer, ForeignKey('user.id'))
    user_relationship = relationship('User')
    likes = relationship('Likes', back_populates='post_rel')
    
class Comment(Base):
    __tablename__ = 'comment'
    id= Column(Integer, primary_key=True)
    comment_text = Column (String(200), nullable=False )
    author_id= Column (Integer, ForeignKey ('user.id'), unique=True)
    author_relationship = relationship('User', back_populates='comment')

class Follow(Base):
   __tablename__ = 'follow'
   user_follower_id= Column (Integer, ForeignKey('user.id'))
   user_following_id = Column (Integer, ForeignKey('user.id'))
   __table_args__ =  (PrimaryKeyConstraint('user_follower_id', 'user_following_id'),)
   user_relationship = relationship('User', back_populates='follow')
     
class Media(Base):
    __tablename__= 'media'
    id= Column(Integer, primary_key=True)
    url= Column(String)
    post_id = Column (Integer, ForeignKey ('post.id')) 
    post_relantionship = relationship ('Post')

class Likes (Base):
     __tablename__ = 'likes'
     post_id = Column (Integer, ForeignKey('post.id'))
     user_id = Column (Integer, ForeignKey('user.id'))
     __table_args__ =  (PrimaryKeyConstraint('post_id', 'user_id'),)
     user_relationship = relationship('User', back_populates='likes')
     post_relationship = relationship('Post', back_populates='likes')


def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
