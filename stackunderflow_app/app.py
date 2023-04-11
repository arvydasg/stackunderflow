import os
from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

basedir = os.path.dirname(os.path.dirname(__file__))

login_manager = LoginManager()
login_manager.login_view = "auth.route_login"
login_manager.login_message_category = "info"
login_manager.login_message = "Please login if you want to see this page"
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        basedir, "db.sqlite"
    )

    flask_secret_key = os.urandom(32)
    app.config["SECRET_KEY"] = flask_secret_key

    from stackunderflow_app.models import db

    login_manager.init_app(app)

    # we are telling SQLAlchemy that this app is going to use this
    # database instance for its database operations
    db.init_app(app)

    # creates an application context for the Flask application, which
    # allows the application to access the necessary resources for
    # database creation
    with app.app_context():
        # creates all the tables defined by the application models
        db.create_all()

    from stackunderflow_app.auth import auth

    app.register_blueprint(auth.bp)

    @app.route("/")
    def route_index():
        return render_template("index.html")

    return app


app = create_app()
