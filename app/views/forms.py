from flask_wtf import FlaskForm as Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class Add_TopicForm(Form):
    title = StringField('Topic Title', validators=[DataRequired()])
    submit = SubmitField('submit')


class Edit_TopicForm(Form):
    title = StringField('Topic Title', validators=[DataRequired()])
    submit = SubmitField('submit')

class Add_ScreenForm(Form):
    text = TextAreaField('Screen Text', validators=[DataRequired()])
    submit = SubmitField('submit')

class Edit_ScreenForm(Form):
    text = TextAreaField('Screen Text', validators=[DataRequired()])
    submit = SubmitField('submit')