from .app import render_template
from flask import Blueprint
from .controllers import VenueController, HomeController, ArtistController, ShowController

routes = Blueprint('routes', __name__)


@routes.route('/')
def home():
    return HomeController.home()


@routes.errorhandler(404)
def not_found_error(error):
    return HomeController.not_found_error(error)


@routes.errorhandler(500)
def server_error(error):
    return HomeController.server_error(error)


class Venues:
    @staticmethod
    @routes.get('/venues')
    def venues():
        return VenueController.index()

    @staticmethod
    @routes.post('/venues/search')
    def venue_search():
        return VenueController.search()

    @staticmethod
    @routes.get('/venues/<int:venue_id>')
    def venue_show(venue_id):
        return VenueController.show(venue_id)

    @staticmethod
    @routes.get('/venues/create')
    def venue_edit():
        return VenueController.create()

    @staticmethod
    @routes.post('/venues/create')
    def venue_store():
        return VenueController.store()

    @staticmethod
    @routes.get('/venues/<int:venue_id>/edit')
    def edit_venue(venue_id):
        return VenueController.edit(venue_id)

    @staticmethod
    @routes.post('/venues/<int:venue_id>/update')
    def venue_update(venue_id):
        return VenueController.update(venue_id)

    @staticmethod
    @routes.delete('/venues/<venue_id>')
    def venue_destroy(venue_id):
        return VenueController.destroy(venue_id)


class Artists:
    @staticmethod
    @routes.get('/artists')
    def artists():
        return ArtistController.index()

    @staticmethod
    @routes.get('/artists/create')
    def artist_create():
        return ArtistController.create()

    @staticmethod
    @routes.post('/artists/create')
    def artist_store():
        return ArtistController.store()

    @staticmethod
    @routes.get('/artists/<int:artist_id>')
    def artist_show(artist_id):
        return ArtistController.show(artist_id)

    @staticmethod
    @routes.get('/artists/<int:artist_id>/edit')
    def artist_edit(artist_id):
        return ArtistController.edit(artist_id)

    @staticmethod
    @routes.post('/artists/<int:artist_id>/update')
    def artist_update(artist_id):
        return ArtistController.update(artist_id)

    @staticmethod
    @routes.post('/artists/search')
    def artist_search():
        return ArtistController.search()


class Shows:
    @staticmethod
    @routes.get('/shows')
    def shows():
        return ShowController.index()

    @staticmethod
    @routes.get('/shows/create')
    def show_create():
        return ShowController.create()

    @staticmethod
    @routes.post('/shows/create')
    def show_store():
        return ShowController.store()
