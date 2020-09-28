from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from flask_admin import Admin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin,db.Model):
  __tablename__='users'
  
  id = db.Column(db.Integer,primary_key =True)
  username = db.Column(db.String())
  email = db.Column(db.String(),unique = True)
  role = db.Column(db.String(100))
  comments = db.relationship('Comment',backref = 'user',lazy="dynamic")
  pass_secure = db.Column(db.String())

  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')
  
  @password.setter
  def password(self,password):
    self.pass_secure = generate_password_hash(password)
  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)
  
  
class BlogPost(db.Model):
  __tablename__='posts'
  
  id = db.Column(db.Integer,primary_key = True)
  post_title = db.Column(db.String())
  post = db.Column(db.String())
  comments = db.relationship('Comment',backref = 'post',lazy="dynamic")

  
class Comment(db.Model):
  __tablename__='comments'
  
  id = db.Column(db.Integer,primary_key = True)
  comment = db.Column(db.String())
  pitch_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  
  
class Quotes:
  '''
  Quotes class
  '''
  
  def __init__(self,author,quote):
    self.author = author
    self.quote = quote