from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):
  comment = TextAreaField('Post a comment',validators=[Required()])
  submit = SubmitField('Post')