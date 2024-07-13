from flask import Flask
from db import db, Book


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

db.init_app(app)





# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD
with app.app_context():
    new_book = Book( title="Assasins Creed", author="Altair", rating=8)
    db.session.add(new_book)
    db.session.commit()

 



