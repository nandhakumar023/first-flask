from config import db

class Contact(db.Model): #it inherits data base model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(180), unique=True, nullable=False)

    def to_json(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "email" : self.email
        }