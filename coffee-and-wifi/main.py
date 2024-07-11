from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from form import CafeForm
import csv
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap5(app)



# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        
        form_data = form.data
        new_data = [value for key, value in form_data.items() if key != 'submit' and key != 'csrf_token']

        with open('cafe-data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_data)
        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        num_columns = len(list_of_rows[0])
    return render_template('cafes.html', cafes=list_of_rows, num_columns=num_columns)


if __name__ == '__main__':
    app.run()
