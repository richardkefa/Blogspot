from flask import redirect,render_template,url_for,request,abort
from . import main
from ..models import User,BlogPost,Comment
from flask_login import login_required,current_user

@main.route('/')
def post():
  title ='Blog Post'
  post = BlogPost.query.all()
  
  return render_template('index.html',posts = posts,title = title)