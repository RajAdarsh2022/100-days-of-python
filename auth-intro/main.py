from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from model import db, User
from flask_login import  login_user, LoginManager, login_required, current_user, logout_user
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
login_manager = LoginManager()

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'



db.init_app(app)
with app.app_context():
    db.create_all()

login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)





@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        password = generate_password_hash(password=request.form.get("password"), method="pbkdf2:sha256", salt_length=8)

        new_user = User(
            email=email,
            name=name,
            password=password
            
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('secrets', name=name))
    return render_template("register.html")


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            user = db.session.execute(db.select(User).where(User.email==email)).scalar()
            
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                print(f"Password for the {user.email} does not match.")
                return f"Invalid Password for {user.email}"
                

        except Exception as e:
            print(f"User with {email} doesn't exist.")
            return "Invalid Username"
        
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    name = current_user.name
    return render_template("secrets.html", name=name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    try:
        return send_from_directory(
            directory='static',
            path='files/cheat_sheet.pdf'
        )
    except Exception as e:
        print(e)
        return "Internal Server error!"


if __name__ == "__main__":
    app.run()
