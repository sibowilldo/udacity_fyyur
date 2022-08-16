from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, DateTimeField
from wtforms.validators import DataRequired
from ...app import db
from ...models import Artist, Venue

artists = map(lambda artist: (artist.id, artist.name),
              db.session.query(Artist).with_entities(Artist.id, Artist.name).all())
venues = map(lambda venue: (venue.id, venue.name),
             db.session.query(Venue).with_entities(Venue.id, Venue.name).all())


class ShowForm(Form):

    name = StringField(
        'name', validators=[DataRequired()]
    )
    artist_id = SelectField(
        'artist_id', validators=[DataRequired()],
        choices=list(artists)
    )
    venue_id = SelectField(
        'venue_id', validators=[DataRequired()],
        choices=list(venues)
    )
    scheduled_at = DateTimeField(
        'scheduled_at',
        validators=[DataRequired()]
    )

    status_is = SelectField(
        # TODO implement enum restriction
        'status_is', validators=[DataRequired()],
        choices=['Draft', 'Scheduled', 'Expired', 'Ongoing', 'Postponed', 'Cancelled']

    )

