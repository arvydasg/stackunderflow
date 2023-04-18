from flask_wtf import FlaskForm

from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_ckeditor import CKEditorField


class AddQuestionForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=140)])
    content = TextAreaField(
        "Your question:", validators=[DataRequired(), Length(max=5000)]
    )


class AddAnswerForm(FlaskForm):
    content = CKEditorField(
        "Your answer:", validators=[DataRequired(), Length(max=5000)]
    )
    submit = SubmitField("Submit")
