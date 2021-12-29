from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired
from wtforms.fields import SelectMultipleField, SelectField

from models import Questions, Interview, User


class UserForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    surname = StringField("Surname")
    password = PasswordField("Password", validators=[DataRequired()])
    is_admin = BooleanField("Admin status", default=False)
    submit = SubmitField("Add")


class InterviewForm(FlaskForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    candidate_name = StringField('Candidate Name', validators=[DataRequired()])
    candidate_surname = StringField('Candidate Surname', validators=[DataRequired()])
    course = SelectMultipleField("Choose Questions", choices=Questions.get_selection_list())
    date_time = DateField('Date of Interview', validators=[DataRequired()])
    link_zoom = StringField('Candidate Name', validators=[DataRequired()])
    total_mark = IntegerField("Maximal Grade", validators=[DataRequired()])
    submit = SubmitField("Add")


class UserInterviewForm(FlaskForm):
    user_login = StringField('User login', validators=[DataRequired()])
    interview_id = IntegerField("Interview Id", validators=[DataRequired()])
    user_comment = StringField('User Comment', validators=[DataRequired()])
    submit = SubmitField("Add")


class InterviewQuestionsForm(FlaskForm):
    interview_id = IntegerField("Interview Id", validators=[DataRequired()])
    question_id = IntegerField("Question Id", validators=[DataRequired()])
    answer = StringField("Answer", validators=[DataRequired()])
    user_mark = IntegerField("Maximal Grade", validators=[DataRequired()], default=10)
    submit = SubmitField("Add")


class QuestionsForm(FlaskForm):
    question = TextAreaField("Question", validators=[DataRequired()])
    course = SelectMultipleField("Choose Course", choices=Questions.get_selection_list())
    kind_of_question = SelectMultipleField("Choose Questions", choices=Questions.get_selection_list())
    submit = SubmitField("Add")


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("Sign In")

