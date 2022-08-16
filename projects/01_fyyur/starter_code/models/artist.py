from .mixins import HasTimestamps
from .pivots import artist_show, artist_genre
from ..app import db, datetime


class Artist(HasTimestamps, db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone = db.Column(db.String(120), nullable=True)
    website = db.Column(db.String(500), nullable=True)
    image_link = db.Column(db.String(500), nullable=True)
    facebook_link = db.Column(db.String(120), nullable=True)
    is_seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(120), nullable=True)

    city_id = db.Column(db.ForeignKey('cities.id'), nullable=False)

    genres = db.relationship('Genre', secondary=artist_genre,
                             lazy='subquery', backref=db.backref('artists', lazy=True))

    shows = db.relationship('Show', secondary=artist_show, collection_class=set,
                            lazy='subquery', backref=db.backref('artists', lazy=True))

    # Filter through all shows and return those with future dates
    def upcoming_shows(self):
        return list(filter(lambda show: show.scheduled_at >= datetime.now(), self.shows))

    # Filter through all shows and return those with past dates
    def past_shows(self):
        return list(filter(lambda show: show.scheduled_at < datetime.now(), self.shows))
