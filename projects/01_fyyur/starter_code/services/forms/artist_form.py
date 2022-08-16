from ...app import Form, StringField, URLField, HiddenField, DataRequired, SelectField, SelectMultipleField, URL, \
    BooleanField
from ...models import City, Genre


def city_choices():
    return map(lambda city: (city.id, city.name), City.query.all())


def genre_choices():
    return map(lambda genre: (genre.id, genre.name), Genre.query.all())


# name phone image_link facebook_link is_seeking_venue seeking description, city_id website
class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    phone = StringField(
        # Todo: Phone Validation
        'phone'
    )
    image_link = URLField(
        'image_link'
    )
    city_id = SelectField(
        'city_id', validators=[DataRequired()],
        choices=list(city_choices())
    )
    facebook_link = URLField(
        'facebook_link', validators=[URL()]
    )
    is_seeking_venue = BooleanField(
        'is_seeking_talent'
    )
    seeking_description = StringField(
        'seeking_description'
    )
    website = URLField(
        'website'
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=list(genre_choices())

    )

