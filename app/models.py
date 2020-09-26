from . import db


class User(db.Model):
  __tablename__='users'
  
  id = db.Column(db.Integer,primary_key =True)
  username = db.Column(db.String())
  email = db.Column(db.String(),unique = True)
  role = db.Column(db.String(100))
  comments = db.relationship('Comment',backref = 'user',lazy="dynamic")

  
  
class BlogPost(db.Model):
  __tablename__='posts'
  
  id = db.Column(db.Integer,primary_key = True)
  post_title = db.Column(db.String())
  post = db.Column(db.String())
  priority = db.Column(db.String())
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  comments = db.relationship('Comment',backref = 'post',lazy="dynamic")

  
class Comment(db.Model):
  __tablename__='comments'
  
  id = db.Column(db.Integer,primary_key = True)
  comment = db.Column(db.String())
  pitch_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))