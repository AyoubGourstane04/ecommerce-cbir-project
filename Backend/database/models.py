from datetime import datetime

from . import db


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)
    image_path = db.Column(db.String(255), nullable=False, unique=True ,default='images/default.png')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'category': self.category,
            'description': self.description,
            'image_path': self.image_path,
            'created_at': self.created_at,
        }