from flask_wtf import Form
from wtforms import TextAreaField, PasswordField, IntegerField, SubmitField, RadioField

class myform(Form):
    password =PasswordField(label="Password")
    username = TextAreaField(label="Username")
    number = IntegerField(label="Phone number")
    Gender = RadioField(label="gender", choices=["Male", "Female"])
    submit = SubmitField("Send")