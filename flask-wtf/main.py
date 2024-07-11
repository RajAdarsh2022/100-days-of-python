from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from form import LoginForm
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
bootstrap = Bootstrap5(app)



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        username_filled = login_form.username.data
        password_filled = login_form.password.data

        if username_filled == os.getenv('ADMIN_USERNAME')  and password_filled == os.getenv('ADMIN_PASSWORD'):
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', login_form=login_form)

if __name__ == '__main__':
    app.run()
