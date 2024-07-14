from flask import Flask, jsonify, render_template, request
from database import db, Cafe
from dotenv import load_dotenv
import random
import os

load_dotenv()

app = Flask(__name__)


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/all")
def get_all_cafes():
    all_cafe_data = db.session.execute(db.select(Cafe)).scalars().all()
    all_cafes = [cafe.to_dict() for cafe in all_cafe_data]

    return jsonify(
        cafes = all_cafes
    ), 200


@app.route("/random")
def get_random_cafe():
    number_of_database_instances = db.session.query(Cafe).count()
    random_instance_index = random.randint(1, number_of_database_instances)

    random_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == random_instance_index)).scalar()

    return jsonify(
        random_cafe.to_dict()
    ), 200

@app.route("/search")
def get_cafes_by_location():
    loc = request.args.get('loc')
    cafes_by_loc_data = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()

    if cafes_by_loc_data == []:
        return jsonify(
            msg = "No cafes as per ur location!"
        ), 404
    else:
        cafes_by_loc = [ cafe.to_dict() for cafe in cafes_by_loc_data]
        return jsonify(
            cafes = cafes_by_loc
        ), 200


@app.route("/add", methods=['POST'])
def add_new_cafe():
    
    new_cafe = Cafe(
        name = request.form['name'],
        map_url = request.form['map_url'],
        img_url = request.form['img_url'],
        location = request.form['location'],
        seats = request.form['seats'],
        has_toilet = bool(request.form['has_toilet']),
        has_wifi = bool(request.form['has_wifi']),
        has_sockets = bool(request.form['has_sockets']),
        can_take_calls = bool(request.form['can_take_calls']),
        coffee_price = request.form.get('coffee_price', None)
    )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(
        mssg = "successfully added"
    ),200


@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_coffee_price(cafe_id):
    new_price = request.args.get('new_price', None)
    
    if new_price == None:
        return jsonify(
            mssg = "New price must be passed as a parameter"
        ), 400
    else:
        try:
            cafe = db.get_or_404(Cafe, cafe_id)
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify(
                mssg = "Data updated successfully"
            ), 200
        except Exception as e:
            print(f"The error was : {e}")
            return jsonify(
                mssg= "Sorry a cafe with that id was not found in the database."
            ), 404


@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get('api-key', None)
    if api_key == os.getenv('API_KEY'):
        try:
            cafe = db.get_or_404(Cafe, cafe_id)
            db.session.delete(cafe)
            db.session.commit()

            return jsonify(
                mssg= "Cafe deleted successfully"
            ), 200

        except Exception as e:
            print(f"The error was : {e}")
            return jsonify(
                mssg= "The cafe that u r looking for doesn't exist"
            ), 404
    else:
        return jsonify(
            mssg= "Sorry, that's not allowed. Make sure you have the correct api-key"
        ), 403


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run()
