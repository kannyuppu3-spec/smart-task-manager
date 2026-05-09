from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

db = SQLAlchemy()

socketio = SocketIO()

def create_app():

    app = Flask(__name__)

    app.config.from_object('app.config.Config')

    db.init_app(app)

    socketio.init_app(app)
    from app.models.user_model import User
    from app.models.task_model import Task
    from app.routes.auth_routes import auth

    
    from app.routes.task_routes import task
    app.register_blueprint(auth)

    app.register_blueprint(task)
    from app.socket import socket_events
    return app