#!/usr/bin/env python3
#server/seed.py

from app import app
from models import db, Pet, Owner
from faker import Faker
from random import choice as rc

with app.app_context():

    # Create and initialize faker generator
    fake = Faker()

    # Delete all rows in pets and owners table every time we seed
    Pet.query.delete()
    Owner.query.delete()

    # Create an empty list
    pets = []
    owners = []

    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Add some Pet instances to the list. Let's add 10
    for n in range(10):
        pets.append(Pet(name = fake.first_name(), species = rc(species)))


    # Insert each Pet in the list into the database table
    db.session.add_all(pets)
    db.session.commit()

    # store all IDs
    ids = [pet.id for pet in Pet.query.all()]

    # Insert Owners

    # Add some Owners instances to the list. Let's add 10
    for n in range(10):
        owners.append(Owner(first_name = fake.first_name(), last_name = fake.last_name(), address = fake.address(), pet_id = rc(ids)))

    # Insert each Owner in the list into the database table
    db.session.add_all(owners)
    db.session.commit()