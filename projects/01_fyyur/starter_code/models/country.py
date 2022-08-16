from .mixins import HasTimestamps
from ..app import db


class Country(HasTimestamps, db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    states_provinces = db.relationship(
        'StateProvince', backref='country', lazy=True, cascade='all, delete')
