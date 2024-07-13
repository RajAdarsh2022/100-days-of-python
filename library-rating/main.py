from flask import Flask, render_template, request, redirect, url_for
from db import db, Books



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db.init_app(app)

with app.app_context():
    db.create_all()



@app.route('/')
def home():
    all_books = list(db.session.execute(db.select(Books)).scalars())
    print(all_books)
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':

        with app.app_context():
            new_book = Books(title = request.form['title'], author = request.form['author'], rating = request.form['rating'])
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')



@app.route("/edit", methods=['GET', 'POST'])
def edit_book_rating():
    book_id = request.args.get('id')
    if request.method == 'POST':
        book = db.session.execute(db.select(Books).filter_by(id = book_id)).scalar_one()
        book.rating = request.form['new_rating']
        db.session.commit()
        return redirect(url_for('home'))
    else:
        book = db.session.execute(db.select(Books).filter_by(id = book_id)).scalar_one()
        return render_template('edit_rating.html', book=book)


@app.route("/delete")
def delete_book():
    book_id = request.args.get('id')
    book = db.session.execute(db.select(Books).filter_by(id = book_id)).scalar_one()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run()

