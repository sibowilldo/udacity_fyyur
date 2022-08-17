from ..app import render_template, request, db, flash, redirect, url_for, jsonify
from ..models import City, Venue, Genre
from ..services.forms import VenueForm


class VenueController:
    def __init__(self):
        pass

    @staticmethod
    def index():

        cities = City.query.filter(City.venues).all()
        return render_template('pages/venues.html', cities=cities)

    @staticmethod
    def show(venue_id):
        venue = Venue.query.filter_by(id=venue_id).first_or_404()
        return render_template('pages/show_venue.html', venue=venue)

    @staticmethod
    def create():
        form = VenueForm()
        return render_template('forms/new_venue.html', form=form)

    @staticmethod
    def store():
        error = False
        form = request.form
        data = {}
        try:
            venue = Venue(name=form['name'], phone=form['phone'], address=form['address'],
                          image_link=form['image_link'],
                          facebook_link=form['facebook_link'],
                          website=form['website'],
                          is_seeking_talent=True if form.get('is_seeking_talent') is not None else False,
                          seeking_description=form['seeking_description'],
                          city_id=form['city_id'])

            for genre in form.getlist('genres'):
                venue.genres.append(Genre.query.get(genre))

            db.session.add(venue)
            data['name'] = venue.name  # Complete: modify data to be the data object returned from db insertion
            db.session.commit()  # Complete: Insert form data as a new Venue record in the db, instead

        except:
            error = True
            db.session.rollback()

        finally:
            db.session.close()
        if not error:  # on successful db insert, flash success
            flash(f'Venue {data["name"]}was successfully listed!', "success")
        else:  # on unsuccessful db insert, flash an error instead.
            flash(f'An error occurred. Venue {data["name"]} could not be listed.')

        return render_template('pages/home.html')

    @staticmethod
    def edit(venue_id):
        form = VenueForm()
        # Complete: populate form with values from venue with ID <venue_id>
        # Jerry rigging this for sure cause wow!
        venue = Venue.query.get(venue_id)
        selected_genres = list(map(lambda genre: genre.id, venue.genres))

        genres = db.session.query(Genre).with_entities(Genre.id, Genre.name).all()
        cities = db.session.query(City).with_entities(City.id, City.name).all()

        data = {
            'cities': cities,
            'genres': genres,
            'selected_genres': selected_genres
        }
        return render_template('forms/edit_venue.html', form=form, venue=venue, data=data)

    @staticmethod
    def update(venue_id):
        error = False
        venue = {}
        form = request.form
        try:
            # Get the venue or fail
            venue = Venue.query.filter(Venue.id == venue_id).first_or_404()
            # Assign new values
            venue.name = form.get('name')
            venue.city_id = form.get('city_id')
            venue.address = form.get('address')
            venue.phone = form.get('phone')
            venue.facebook_link = form.get('facebook_link')
            venue.image_link = form.get('image_link')
            venue.website = form.get('website')
            venue.is_seeking_talent = True if form.get('is_seeking_talent') else False
            venue.seeking_description = form.get('seeking_description')
            # Delete existing relationships
            venue.genres = []
            # Assign new relationships
            for genre in form.getlist('genres'):
                venue.genres.append(Genre.query.get(genre))
            # Commit Changes
            db.session.commit()
        except:
            error = True
            db.session.rollback()
        finally:
            db.session.close()
        if error:
            flash(f'Error! Something went wrong trying to save {form.get("name")}', 'danger')
        else:
            venue = Venue.query.get(venue_id)
            flash(f'Success, {venue.name} details were updated!', 'success')
        # Complete: take values from the form submitted, and update existing
        # venue record with ID <venue_id> using the new attributes
        return redirect(url_for('venues.show', venue_id=venue_id))

    @staticmethod
    def destroy():
        error = False
        data = {}
        try:
            venue = Venue.query.filter(Venue.id == request.json['venue_id']).first_or_404()
            data['name'] = venue.name
            venue.shows = []
            venue.genres = []
            db.session.delete(venue)
            db.session.commit()
            data['redirect_to'] = url_for('routes.home')
        except:
            error = True
            data['redirect_to'] = url_for('venues.edit', venue_id=request.form['venue_id'])
            db.session.rollback()
        finally:
            db.session.close()

        if error:
            data['flash'] = f'Error! Something went wrong while trying to delete Venue'
        else:
            data['flash'] = f'{data["name"]} was deleted successfully'

        # Complete: Complete this endpoint for taking a venue_id, and using
        # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.

        # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
        # clicking that button delete it from the db then redirect the user to the homepage
        print(data)
        return data

    @staticmethod
    def search():
        # Complete: implement search on venues with partial string search. Ensure it is case-insensitive.
        search_term = request.form.get('search_term', '')
        venues = Venue.query.filter(Venue.name.ilike(f'%{search_term}%')).all()
        response = {
            "count": len(venues),
            "data": venues
        }
        return render_template('pages/search_venues.html', results=response,
                               search_term=request.form.get('search_term', ''))
