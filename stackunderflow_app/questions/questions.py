from flask import render_template, request, redirect, url_for, flash
from stackunderflow_app.models import db, Users, Question
from stackunderflow_app.questions.question_form import AddQuestionForm
from stackunderflow_app.app import login_manager, bcrypt
from flask_login import current_user, logout_user, login_user, login_required

from flask import Blueprint

bp = Blueprint("questions", __name__, url_prefix="/questions")


@login_manager.user_loader
def load_user(users_id):
    return Users.query.get(int(users_id))


@bp.route("/all_questions", methods=["GET", "POST"])
def route_all_questions():
    """Route for register page."""
    questions = Question.query.all()
    return render_template("questions/all_questions.html", questions=questions)


@bp.route("/new_question", methods=["GET", "POST"])
@login_required
def route_add_new_question():
    """Route for adding a new question."""
    form = AddQuestionForm()
    if form.validate_on_submit():
        new_question = Question(
            title=form.title.data, content=form.content.data, author_id=current_user.id
        )
        db.session.add(new_question)
        db.session.commit()
        flash("You have successfully asked a question!")
        return redirect(url_for("questions.route_all_questions"))
    return render_template("questions/new_question.html", form=form)
