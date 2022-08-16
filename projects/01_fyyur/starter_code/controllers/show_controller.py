from ..app import render_template, flash, request, db, redirect, url_for
from ..models import Show, Artist, Venue
from ..services.forms import ShowForm


class ShowController:
    def __init__(self):
        pass

    @staticmethod
    def index():
        # displays list of shows at /shows
        # Complete: replace with real venues data.
        data = Show.query.order_by(Show.scheduled_at.desc()).all()
        return render_template('pages/shows.html', shows=data)

    @staticmethod
    def create():
        # renders form. do not touch.
        form = ShowForm()
        return render_template('forms/new_show.html', form=form)

    @staticmethod
    def store():
        print(request.form)
        error = False
        # called to create new shows in the db, upon submitting new show listing form
        # Complete: insert form data as a new Show record in the db, instead
        try:
            venue = Venue.query.filter_by(id=request.form.get('venue_id')).first_or_404()
            artist = Artist.query.filter_by(id=request.form.get('artist_id')).first_or_404()
            show = Show()
            show.name = request.form.get('name')
            show.scheduled_at = request.form.get('scheduled_at')
            show.status_is = request.form.get('status_is')

            show.venues.append(venue)
            show.artists.append(artist)
            db.session.add(show)
            db.session.commit()
        except:
            error = True
            db.session.rollback()
        finally:
            db.session.close()
        if error:
            flash(u'An error occurred. Show could not be listed.', 'danger')
            # Complete: on unsuccessful db insert, flash an error instead.
        else:
            # on successful db insert, flash success
            flash('Show was successfully listed!', 'success')
        return redirect(url_for('routes.home'))
