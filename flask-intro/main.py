from flask import Flask
from flask import render_template
import random

app = Flask(__name__)
random_number = random.randint(0,9)


@app.route("/")
def home():
    return render_template('index.html')



if __name__ == "__main__":
    app.run()