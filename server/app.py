# server/app.py

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Pet

'''
    DATABASE CONFIGURATION
'''

# create a Flask application instance 
app = Flask(__name__)

# configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# configure flag to disable modification tracking and use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#configures json not to be displayed in a single line
app.json.compact = False

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)

'''
    SERVING DATABASE RECORDS IN FLASK APP
'''

@app.route('/')
def index():
    response_body = {
        'message' : 'Welcome to the Pet directorate'
    }
    response = make_response(
        response_body,
        200
    )
    return response

@app.route('/pets/<int:id>')
def pet_by_id(id):
    pet = Pet.query.filter(Pet.id == id).first()
    if pet:
        response_body = pet.to_dict()
        response_status = 200
    else:
        response_body = {
            'message' : f'Pet of ID:{id} not found'
        }
        response_status = 404

    response = make_response(
        response_body,
        response_status,
    )
    return response

@app.route('/pets/<string:species>')
def pet_by_species(species):
    pets_db = Pet.query.filter_by(species = species).all()
    pets = []

    if pets_db:
        for pet in pets_db:
            pets.append(pet.to_dict())
        
        response_body = {
            'count' : len(pets),
            'pets' : pets
        }
        response_status = 200
    else:
        response_body = {
            'message' : f'Pet of species: {species} not found'
        }
        response_status = 404

    response = make_response(
        response_body,
        response_status,
    )
    return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)
