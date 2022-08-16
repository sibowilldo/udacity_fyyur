from .routes import routes
from .app import app
app.register_blueprint(routes)
