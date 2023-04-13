from flask import render_template, request, redirect, url_for, flash
from stackunderflow_app.models import db, Users, Question, Answer
from stackunderflow_app.questions.question_form import AddAnswerForm
from stackunderflow_app.app import login_manager
from flask_login import current_user, login_required
from stackunderflow_app.questions.questions import bp


@bp.route("/<int:question_id>/answer_question", methods=["GET", "POST"])
@login_required
def route_answer_question(question_id):
    """Route for answering a question."""
    question = Question.query.get_or_404(question_id)
    form = AddAnswerForm()
    if form.validate_on_submit():
        new_answer = Answer(
            content=form.content.data,
            author_id=current_user.id,
            question_id=question_id,
        )
        db.session.add(new_answer)
        db.session.commit()
        flash("You have successfully answered the question!")
        return redirect(
            url_for("questions.route_question_detail", question_id=question_id)
        )
    return render_template("answers/answer_question.html", form=form, question=question)


@bp.route(
    "/<int:question_id>/answer_question/edit_answer/<int:answer_id>",
    methods=["GET", "POST"],
)
@login_required
def route_edit_answer(question_id, answer_id):  # fetching from the url
    """Route for editing an answer."""
    answer = Answer.query.filter_by(
        id=answer_id, question_id=question_id
    ).first_or_404()
    question = Question.query.get_or_404(question_id)
    if current_user.id != answer.author_id:
        flash("You can only edit your own answers!")
        return redirect(url_for("questions.route_all_questions"))
    form = AddAnswerForm(obj=answer)  # fill fields with data
    if form.validate_on_submit():
        answer.content = form.content.data
        db.session.commit()
        flash("You have successfully edited an answer!")
        return redirect(
            url_for("questions.route_question_detail", question_id=question_id)
        )
    return render_template(
        "answers/edit_answer.html",
        form=form,
        answer=answer,
        question_id=question_id,
        question=question,
    )


# This route is accessible only through a POST request. Preventing accidental deletion
@bp.route("/<int:question_id>/delete_answer/<int:answer_id>", methods=["POST"])
@login_required
def route_delete_answer(
    question_id, answer_id
):  # fetching answer_id parameter from the url
    """Route for deleting a answer."""
    answer = Answer.query.get_or_404(answer_id)
    if current_user.id != answer.author_id:
        flash("You can only delete your own answers!")
        return redirect(
            url_for("questions.route_question_detail", question_id=question_id)
        )
    db.session.delete(answer)
    db.session.commit()
    flash("You have successfully deleted the answer!")
    return redirect(url_for("questions.route_question_detail", question_id=question_id))
