from app import db
from datetime import datetime

class Task(db.Model):

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)

    description = db.Column(db.Text)

    priority = db.Column(db.String(20))

    status = db.Column(db.String(20))

    created_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):

        return f"<Task {self.title}>"