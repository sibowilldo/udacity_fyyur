from ..app import db, datetime
from .pivots import genre_venue, show_venue
from .mixins import HasTimestamps


class Venue(HasTimestamps, db.Model):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String(500), nullable=True)
    image_link = db.Column(db.String(500), nullable=True)
    facebook_link = db.Column(db.String(120), nullable=True)
    is_seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(120), nullable=True)

    city_id = db.Column(db.ForeignKey('cities.id'), nullable=False)

    genres = db.relationship('Genre', secondary=genre_venue,
                             lazy='subquery', backref=db.backref('venues', lazy=True))

    shows = db.relationship('Show', secondary=show_venue, collection_class=set,
                            lazy='subquery', backref=db.backref('venues', lazy=True))

    def __repr__(self) -> str:
        return f'<Venue {self.id} {self.name} {self.genres}>'

    # Filter through all shows and return those with future dates
    def upcoming_shows(self):
        return list(filter(lambda show: show.scheduled_at >= datetime.now(), self.shows))

    # Filter through all shows and return those with past dates
    def past_shows(self):
        return list(filter(lambda show: show.scheduled_at < datetime.now(), self.shows))
