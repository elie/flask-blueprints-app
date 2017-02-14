from project import db

class Superhero(db.Model):

    __tablename__ = 'superheroes'

    # DDL
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    # DML
    def __init__(self, name):
        self.name = name