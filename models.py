from app import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    director = db.Column(db.String(100))
    year = db.Column(db.Integer)
    synopsis = db.Column(db.Text)
