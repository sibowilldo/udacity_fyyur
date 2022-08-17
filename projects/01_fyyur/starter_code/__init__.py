from .routes.routes import routes, venues, artists, shows
from .app import app
app.register_blueprint(routes)
app.register_blueprint(venues)
app.register_blueprint(artists)
app.register_blueprint(shows)
