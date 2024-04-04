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

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)

'''
    SERVING DATABASE RECORDS IN FLASK APP
'''

@app.route('/pets/<int:id>')
def pet_by_id(id):
    pet = Pet.query.filter(Pet.id == id).first()
    if pet:
        response_body = f'<p>{pet.name} {pet.species}'
        response_status = 200
    else:
        response_body = f'<p>Pet {id} not found'
        response_status = 404

    response = make_response(
        response_body,
        response_status,
    )
    return response

@app.route('/pets/<string:species>')
def pet_by_species(species):
    pets = Pet.query.filter_by(species = species).all()
    response_body = f'<p>There are {len(pets)} {species}\'s</p>'

    if pets:
        for pet in pets:
            response_body += f'<p>{pet.name} | {pet.species}</p>'
        response_status = 200
    else:
        response_body = f'<p>Pet {species} not found'
        response_status = 404

    response = make_response(
        response_body,
        response_status,
    )
    return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)
