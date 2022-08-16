from .mixins import HasTimestamps
from ..app import db


class StateProvince(HasTimestamps, db.Model):
    __tablename__ = 'states_provinces'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    country_id = db.Column(db.ForeignKey('countries.id'), nullable=False)
    cities = db.relationship(
        'City', backref='state_province', lazy=True, cascade='all, delete')
