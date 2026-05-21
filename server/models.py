from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)


# Earthquake model
class Earthquake(db.Model):
    __tablename__ = "earthquakes"

    # Primary key ID
    id = db.Column(db.Integer, primary_key=True)

    # Earthquake magnitude
    magnitude = db.Column(db.Float)

    # Location of earthquake
    location = db.Column(db.String)

    # Year earthquake occurred
    year = db.Column(db.Integer)

    # String representation of the model
    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"