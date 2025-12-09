from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)

#this creates the tables from the models file if they don't exist already
    with app.app_context():
        db.create_all()
        from . import models