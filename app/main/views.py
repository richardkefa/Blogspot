from flask import redirect,render_template,url_for,request,abort
from . import main
from ..models import User,BlogPost,Comment
from flask_login import login_required,current_user
from .forms import CommentForm,BlogForm
from .. import db
from ..request import get_quotes


@main.route('/')
def post():
  title ='Blog Post'
  quotes = get_quotes()
  posts = BlogPost.query.all()
  
  return render_template('index.html',quotes = quotes,posts = posts,title = title)

@main.route('/comment/<int:post_id>',methods = ['POST','GET'])
@login_required
def comment(post_id):
  form = CommentForm()
  post = BlogPost.query.get(post_id)
  post_comment = Comment.query.filter_by(post_id=post_id).all()
  
  if form.validate_on_submit():
    comment = form.comment.data
    post_id = post_id
    user_id = current_user._get_current_object().id
    new_comment = Comment(comment=comment,user_id=user_id,post_id=post_id)
    new_comment.save_comment()
    return redirect(url_for('.comment', post_id = post_id))
    
  return render_template('comments.html', form = form, post=post, post_comment=post_comment)

@main.route('/new_post', methods=['POSt','GET'])
def new_blog():
  form = BlogForm()
  if form.validate_on_submit():
    post_title = form.title.data
    post = form.post.data
    user_id = current_user._get_current_object().import ipdb; ipdb.set_trace()
    blog = Blog(post_title=post_title,post=post,user_id=user_id)
    blog.saveblog()
    flash('you have posted a new blog')
    
  return render_template('newblog.html',form = form)
  
  
@main.route('/blog_update/<blog_id>', methods = ['GET' , 'POST'])
def updateblog(post_id):
  blog = BlogPost.query.get(post_id)
  if blog.