from ..app import render_template, request, db, flash, redirect, url_for
from ..models import City, Venue, Genre, Artist
from ..services.forms import ArtistForm


class ArtistController:
    def __init__(self):
        pass

    @staticmethod
    def index():
        # Complete: replace with real data returned from querying the database
        data = db.session.query(Artist).with_entities(Artist.id, Artist.name)
        return render_template('pages/artists.html', artists=data)

    @staticmethod
    def create():
        form = ArtistForm()
        return render_template('forms/new_artist.html', form=form)

    @staticmethod
    def store():
        # called upon submitting the new artist listing form
        # Complete: insert form data as a new Venue record in the db, instead
        # Complete: modify data to be the data object returned from db insertion
        error = False
        form = request.form
        data = {}
        try:
            artist = Artist(
                name=form.get('name'), phone=form.get('phone'),
                image_link=form.get('image_link'),
                facebook_link=form.get('facebook_link'),
                website=form.get('website'),
                is_seeking_venue=True if form.get('is_seeking_venue') is not None else False,
                seeking_description=form.get('seeking_description'),
                city_id=form.get('city_id'))

            for genre in form.getlist('genres'):
                artist.genres.append(Genre.query.get(genre))

            db.session.add(artist)
            data['name'] = artist.name  # Complete: modify data to be the data object returned from db insertion
            db.session.commit()  # Complete: Insert form data as a new Venue record in the db, instead

        except:
            error = True
            db.session.rollback()
        finally:
            db.session.close()

        if error:
            # Complete: on unsuccessful db insert, flash an error instead.
            flash('An error occurred. Artist ' + form.get('name') + ' could not be listed.')
        else:
            # on successful db insert, flash success
            flash('Artist ' + data['name'] + ' was successfully listed!')

        return render_template('pages/home.html')

    @staticmethod
    def show(artist_id):
        # shows the artist page with the given artist_id
        # Complete: replace with real artist data from the artist table, using artist_id

        artist = Artist.query.filter_by(id=artist_id).first_or_404()
        return render_template('pages/show_artist.html', artist=artist)

    @staticmethod
    def edit(artist_id):
        form = ArtistForm()
        # Yet Another! Jerry rigging this for sure cause wow!
        artist = Artist.query.get(artist_id)

        selected_genres = list(map(lambda genre: genre.id, artist.genres))

        genres = db.session.query(Genre).with_entities(Genre.id, Genre.name).all()
        cities = db.session.query(City).with_entities(City.id, City.name).all()

        data = {
            'cities': cities,
            'genres': genres,
            'selected_genres': selected_genres
        }

        # Complete: populate form with fields from artist with ID <artist_id>
        return render_template('forms/edit_artist.html', form=form, artist=artist, data=data)

    @staticmethod
    def update(artist_id):
        error = False
        form = request.form
        try:
            # Get the artist or fail
            artist = Artist.query.filter(Artist.id == artist_id).first_or_404()
            # Assign new values
            artist.name = form.get('name')
            artist.phone = form.get('phone')
            artist.image_link = form.get('image_link')
            artist.facebook_link = form.get('facebook_link')
            artist.is_seeking_venue = True if form.get('is_seeking_venue') else False
            artist.seeking_description = form.get('seeking_description')
            artist.city_id = form.get('city_id')
            artist.website = form.get('website')
            # Delete existing relationships
            artist.genres = []
            # Assign new relationships
            print(form.getlist('genres'))
            for genre in form.getlist('genres'):
                artist.genres.append(Genre.query.get(genre))
            # Commit Changes
            db.session.commit()
        except:
            error = True
            db.session.rollback()
        finally:
            db.session.close()
        if error:
            flash(f'Error! Something went wrong trying to save { form.get("name") }')
        else:
            artist = Artist.query.filter_by(id=artist_id).first_or_404()
            flash(f'Success, {artist.name} details were updated!')

        # Complete: take values from the form submitted, and update existing

        return redirect(url_for('routes.artist_show', artist_id=artist_id))

    @staticmethod
    def search():
        # Complete: implement search on artists with partial string search. Ensure it is case-insensitive.
        # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
        # search for "band" should return "The Wild Sax Band".
        search_term = request.form.get('search_term', '')
        artist = Artist.query.filter(Artist.name.ilike(f'%{search_term}%')).all()
        response = {
            "count": len(artist),
            "data": artist
        }
        return render_template('pages/search_artists.html', results=response,
                               search_term=request.form.get('search_term', ''))
