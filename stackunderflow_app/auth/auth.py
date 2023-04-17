from flask import render_template, request, redirect, url_for, flash
from stackunderflow_app.models import db, Users, Question
from stackunderflow_app.auth.auth_forms import (
    RegisterForm,
    LoginForm,
    UpdateProfileInformation,
)
from stackunderflow_app.app import login_manager, bcrypt
from flask_login import current_user, logout_user, login_user, login_required

from flask import Blueprint

bp = Blueprint("auth", __name__, url_prefix="/auth")


@login_manager.user_loader
def load_user(users_id):
    return Users.query.get(int(users_id))


@bp.route("/register", methods=["GET", "POST"])
def route_register():
    """Route for register page."""
    form = RegisterForm()

    if form.validate_on_submit():
        encrypted_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        new_user = Users(
            name=form.name.data, email=form.email.data, password=encrypted_password
        )
        db.session.add(new_user)
        db.session.commit()
        flash("You have successfully registered 🙏 You can login now.")
        return redirect(url_for("auth.route_login"))
    return render_template("auth/register.html", form=form)


@bp.route("/login", methods=["GET", "POST"])
def route_login():
    """Route for login page."""
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for("index"))

    if form.validate_on_submit():
        user = Users.query.filter_by(name=form.name.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("You have successfully logged in.")
            return redirect(url_for("route_index"))
        else:
            flash("Prisijungti nepavyko. Patikrinkite prisijungimo vardą ir slaptažodį")
    return render_template("auth/login.html", form=form)


@bp.route("/logout", methods=["GET", "POST"])
def route_logout():
    """Route for logging out."""
    if current_user.is_authenticated:
        logout_user()
        flash("You have been successfully logged out 🙏")
        return redirect(url_for("auth.route_login"))
    else:
        return render_template("index.html")


@bp.route("/my_account", methods=["GET", "POST"])
@login_required
def route_my_account():
    form = UpdateProfileInformation()

    # if I place this at the top of the file - circular import.. too
    # tired of trying to figure it out. At least it works now.
    from stackunderflow_app.other_scripts import save_picture

    if form.validate_on_submit():
        if form.profile_image.data:
            new_profile_image = save_picture(form.profile_image.data)
            current_user.profile_image = new_profile_image
        current_user.name = form.name.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account information has been updated!", "success")
        return redirect(url_for("auth.route_my_account"))
    elif request.method == "GET":
        form.name.data = current_user.name
        form.email.data = current_user.email

    questions = Question.query.filter_by(author=current_user).all()

    new_profile_image = url_for(
        "static", filename="profile_images/" + current_user.profile_image
    )
    return render_template(
        "auth/my_account.html",
        title="Account",
        form=form,
        profile_image=new_profile_image,
        questions=questions,
    )
