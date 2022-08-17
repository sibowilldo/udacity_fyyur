from ..app import render_template
from flask import Blueprint
from ..controllers import VenueController, HomeController, ArtistController, ShowController

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

# Complete: [VS-1] Apply Blueprints to All Routes, then...
# Complete: [VS-2] Update all Affected Controllers, then...
# Complete: [VS-3] Update all affected Templates

venues=Blueprint('venues', __name__, url_prefix='/venues')
class Venues:
    @staticmethod
    @venues.get('/')
    def index():
        return VenueController.index()

    @staticmethod
    @venues.post('/search')
    def search():
        return VenueController.search()

    @staticmethod
    @venues.get('/<int:venue_id>')
    def show(venue_id):
        return VenueController.show(venue_id)

    @staticmethod
    @venues.get('/create')
    def create():
        return VenueController.create()

    @staticmethod
    @venues.post('/create')
    def store():
        return VenueController.store()

    @staticmethod
    @venues.get('/<int:venue_id>/edit')
    def edit(venue_id):
        return VenueController.edit(venue_id)

    @staticmethod
    @venues.post('/<int:venue_id>/update')
    def update(venue_id):
        return VenueController.update(venue_id)

    @staticmethod
    @venues.delete('/delete')
    def destroy():
        return VenueController.destroy()

artists= Blueprint('artists', __name__,url_prefix='/artists')
class Artists:
    @staticmethod
    @artists.get('/')
    def index():
        return ArtistController.index()

    @staticmethod
    @artists.get('/create')
    def create():
        return ArtistController.create()

    @staticmethod
    @artists.post('/create')
    def store():
        return ArtistController.store()

    @staticmethod
    @artists.get('/<int:artist_id>')
    def show(artist_id):
        return ArtistController.show(artist_id)

    @staticmethod
    @artists.get('/<int:artist_id>/edit')
    def edit(artist_id):
        return ArtistController.edit(artist_id)

    @staticmethod
    @artists.post('/<int:artist_id>/update')
    def update(artist_id):
        return ArtistController.update(artist_id)

    @staticmethod
    @artists.post('/search')
    def search():
        return ArtistController.search()

shows=Blueprint('shows', __name__, url_prefix='/shows')
class Shows:
    @staticmethod
    @shows.get('/')
    def index():
        return ShowController.index()

    @staticmethod
    @shows.get('/create')
    def create():
        return ShowController.create()

    @staticmethod
    @shows.post('/create')
    def store():
        return ShowController.store()
