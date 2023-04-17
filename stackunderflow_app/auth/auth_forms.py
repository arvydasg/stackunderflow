"""All the flask_wtf forms reside here."""

from flask_wtf import FlaskForm

# from flask_wtf.file import FileField, FileAllowed
from wtforms import (
    SubmitField,
    StringField,
    PasswordField,
    TextAreaField,
    BooleanField,
    validators,
    DateField,
    TimeField,
)
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError
from stackunderflow_app.models import Users

from flask_login import current_user


class RegisterForm(FlaskForm):
    """Register form."""

    name = StringField(
        "Name:",
        validators=[
            DataRequired(),
            Length(min=4, message="Username must contain at least 4 symbols."),
        ],
    )
    email = StringField(
        "Email:", validators=[DataRequired(), Email(message="Wrong email format.")]
    )
    password = PasswordField(
        "Password:",
        validators=[
            DataRequired(),
            Length(min=4, message="Password must contain at least 4 symbols."),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password:",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )
    submit = SubmitField("Submit")

    def validate_name(self, name):
        user = Users.query.filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError("This username is already taken.")

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("This email address is already registered.")


class LoginForm(FlaskForm):
    """Login form."""

    name = StringField("Name:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])
    submit = SubmitField("Submit")


class UpdateProfileInformation(FlaskForm):
    """Form used to update profile information."""

    name = StringField("Name:", [DataRequired()])
    email = StringField("Email:", [DataRequired()])
    profile_image = FileField(
        "Update profile image:", validators=[FileAllowed(["jpg", "png"])]
    )
    submit = SubmitField("Update")

    def validate_name(self, name):
        if name.data != current_user.name:
            user = Users.query.filter_by(name=name.data).first()
            if user is not None:
                raise ValidationError("This name is already taken.")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user is not None:
                raise ValidationError("This email address is already registered.")
