from ..app import db


show_venue = db.Table('show_venue',
                      db.Column('show_id', db.Integer, db.ForeignKey('shows.id'), primary_key=True),
                      db.Column('venue_id', db.Integer, db.ForeignKey('venues.id'), primary_key=True))


genre_venue = db.Table('genre_venue',
                       db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True),
                       db.Column('venue_id', db.Integer, db.ForeignKey('venues.id'), primary_key=True))


artist_genre = db.Table('artist_genre',
                        db.Column('artist_id', db.Integer, db.ForeignKey('artists.id'), primary_key=True),
                        db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True))


artist_show = db.Table('artist_show',
                       db.Column('artist_id', db.Integer, db.ForeignKey('artists.id'), primary_key=True),
                       db.Column('show_id', db.Integer, db.ForeignKey('shows.id'), primary_key=True))
