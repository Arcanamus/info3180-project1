from . import db

class PropertyProfile(db.Model):

    __tablename__ = 'property_profile'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    bedrooms = db.Column(db.String())
    bathrooms = db.Column(db.String())
    price = db.Column(db.String())
    type = db.Column(db.String())
    location = db.Column(db.String())
    photo = db.Column(db.String())
    
    def __init__(self, title, description, bedrooms, bathrooms, price, type, location, photo):
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price
        self.type = type
        self.location = location
        self.photo = photo