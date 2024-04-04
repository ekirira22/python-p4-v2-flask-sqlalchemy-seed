from models import db, SerializerMixin

# define a model class by inheriting from db.Model.
class Owner(db.Model, SerializerMixin):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)
    address = db.Column(db.String)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'), nullable=False)

    def __repr__(self) -> str:
        return f'<Owner {self.id}, {self.first_name}, {self.last_name}, {self.address}>'