from .mixins import HasTimestamps
from ..app import db


class City(HasTimestamps, db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    state_province_id = db.Column(db.ForeignKey(
        'states_provinces.id'), nullable=False)

    venues = db.relationship('Venue', backref='city',
                             lazy='joined', cascade='all, delete')

    artists = db.relationship('Artist', backref='city',
                             lazy='joined', cascade='all, delete')

    def __repr__(self) -> str:
        return f'<City {self.id} {self.name} {self.venues}>'
