import os
from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
import json
import urllib3

with open("./config.json") as config_file:
    config = json.load(config_file)

basedir = os.path.dirname(os.path.dirname(__file__))

login_manager = LoginManager()
login_manager.login_view = "auth.route_login"
login_manager.login_message_category = "info"
login_manager.login_message = "Please login if you want to see this page"
bcrypt = Bcrypt()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    ckeditor = CKEditor(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        basedir, config.get("SQLALCHEMY_DATABASE_URI")
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SECRET_KEY"] = config.get("SECRET_KEY")

    from stackunderflow_app.models import db

    login_manager.init_app(app)

    # we are telling SQLAlchemy that this app is going to use this
    # database instance for its database operations
    db.init_app(app)
    migrate.init_app(app, db)

    # creates an application context for the Flask application, which
    # allows the application to access the necessary resources for
    # database creation
    with app.app_context():
        # creates all the tables defined by the application models
        db.create_all()

    from stackunderflow_app.auth import auth

    app.register_blueprint(auth.bp)

    from stackunderflow_app.questions import questions
    from stackunderflow_app.answers import answers

    from flask_admin import Admin
    from flask_admin.contrib.sqla import ModelView
    from flask_login import current_user
    from stackunderflow_app.models import Users, Question, Answer, Action

    class MyModelView(ModelView):
        def is_accessible(self):
            return current_user.is_authenticated and current_user.name == config.get(
                "ADMIN_USER_NAME"
            )

    admin = Admin(app)
    admin.add_view(MyModelView(Users, db.session))
    admin.add_view(MyModelView(Question, db.session))
    admin.add_view(MyModelView(Answer, db.session))
    admin.add_view(MyModelView(Action, db.session))

    app.register_blueprint(questions.bp)

    @app.route("/")
    def route_index():
        return render_template("index.html")

    @app.errorhandler(404)
    def page_not_found(e):
        return (render_template("errors/404.html"), 404)

    # Internal server error
    @app.errorhandler(500)
    def page_not_found(e):
        return render_template("errors/500.html"), 500

    return app


app = create_app()
