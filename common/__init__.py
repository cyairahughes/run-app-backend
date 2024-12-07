from flask import Flask, logging
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth
import jwt


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/cyair/run-app-backend/database.db"
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    return app

app = create_app()
db = SQLAlchemy(app)
log = logging.create_logger(app)
auth = HTTPTokenAuth(scheme='Bearer')


@auth.verify_token
def verify_token(token):
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        current_user = str(data['user_id'])
    except Exception:
        return None
    return current_user