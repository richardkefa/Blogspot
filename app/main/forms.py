from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import Required

class CommentForm(FlaskForm):
  comment = TextAreaField('Post a comment',validators=[Required()])
  submit = SubmitField('Post')
  
class BlogForm(FlaskForm):
  post_title = StringField('Blog title',validators=[Required()])
  post = TextAreaField('Blog content',validators=[Required()])
  submit = SubmitField('Post')