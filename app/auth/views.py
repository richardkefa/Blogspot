from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user,login_required
from flask_admin.contrib.sqla import ModelView
from ..models import User,BlogPost,Comment
from .forms import RegistrationForm,LoginForm
from .. import db,admin,main
from . import auth
from ..email import mail_message

@auth.route('/register',methods=["GET","POST"])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(email = form.email.data, username = form.username.data,password = form.password.data)
    db.session.add(user)
    db.session.commit()
    mail_message("Welcome to The insight","email/welcome_user",user.email,user=user)
    return redirect(url_for('auth.login'))
  return render_template('auth/register.html',form = form)
  
  
@auth.route('/login',methods=["GET","POST"])
def login():
  login_form=LoginForm()
  if login_form.validate_on_submit():
    user = User.query.filter_by(username=login_form.username.data).first()
    if user is'admin' and user.verify_password(login_form.password.data):
      
      return redirect(request.args.get('next') or url_for('auth.admin'))
    
    elif user is not None and user.verify_password(login_form.password.data):
      login_user(user,login_form.remember.data)
      return redirect(request.args.get('next') or url_for('main.post'))
    flash('Invalid username or password')
  title = "Blog Login"
  return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for("main.post"))

class MyModelView(ModelView):
  def is_accessible(self):
    
    return True  
@auth.route('/admin') 
admin():
#creating admin view
  admin.add_view(MyModelView(User,db.session))
  admin.add_view(MyModelView(BlogPost,db.session))
  admin.add_view(MyModelView(Comment,db.session))
return admin

    