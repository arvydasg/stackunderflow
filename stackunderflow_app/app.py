import os
from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

basedir = os.path.dirname(os.path.dirname(__file__))

login_manager = LoginManager()
login_manager.login_view = "auth.route_login"
login_manager.login_message_category = "info"
login_manager.login_message = "Please login if you want to see this page"
bcrypt = Bcrypt()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        basedir, "db.sqlite"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    flask_secret_key = os.urandom(32)
    app.config["SECRET_KEY"] = flask_secret_key

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
