from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, ValidationError

class PostForm(FlaskForm):
    post_box = TextAreaField("Insert your post here", widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField("Post")
    
    def validate_post_box(self, post_box):
        if len(post_box.data) > 280:
            raise ValidationError("Your post cannot be longer than 280 characters.")