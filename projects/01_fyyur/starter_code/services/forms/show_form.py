from ...app import Form, StringField, URLField, HiddenField, DataRequired, SelectField, SelectMultipleField, URL, BooleanField
from ...models import City, Genre


def city_choices():
    return map(lambda city: (city.id, city.name), City.query.all())


def genre_choices():
    return map(lambda genre: (genre.id, genre.name), Genre.query.all())


class ShowForm(Form):
    _token = HiddenField('csrf_token')

    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = SelectField(
        'city', validators=[DataRequired()],
        choices=list(city_choices())
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone'
    )
    image_link = URLField(
        'image_link'
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=list(genre_choices())

    )
    facebook_link = URLField(
        'facebook_link', validators=[URL()]
    )
    website = URLField(
        'website'
    )

    is_seeking_talent = BooleanField('is_seeking_talent')

    seeking_description = StringField(
        'seeking_description'
    )

