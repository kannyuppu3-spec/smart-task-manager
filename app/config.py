class Config:

    SECRET_KEY = "secret123"

    SQLALCHEMY_DATABASE_URI = \
        "postgresql://postgres:root@localhost/taskdb"

    SQLALCHEMY_TRACK_MODIFICATIONS = False