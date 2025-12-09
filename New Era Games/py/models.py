from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Game(db.Model):
    __tablename__= 'games'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    dev = db.Column(db.String(255), nullable=False)
    avatar = db.Column(db.LargeBinary, nullable=False)
    cover = db.Column(db.LargeBinary, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    tags = db.Column(db.JSON, nullable=False)
    link = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        """Convertir objeto a diccionario para JSON con imágenes en base64"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'dev': self.dev,
            'avatar': base64.b64encode(self.avatar).decode('utf-8') if self.avatar else None,
            'cover': base64.b64encode(self.cover).decode('utf-8') if self.cover else None,
            'category': self.category,
            'tags': self.tags,
            'link': self.link
        }
