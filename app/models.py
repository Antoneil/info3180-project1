from app import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    property_type = db.Column(db.String(50), nullable=False)
    photo = db.Column(db.String(255)) 

    def __init__(self, title, description, bedrooms, bathrooms, location, price, property_type, photo=None):
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.property_type = property_type
        self.photo = photo

    def __repr__(self):
        return f"Property('{self.title}', '{self.location}', '{self.price}')"
