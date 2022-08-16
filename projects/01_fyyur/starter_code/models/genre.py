from .mixins import HasTimestamps
from ..app import db


class Genre(HasTimestamps, db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return f'(id:{self.id}, name:{self.name})'
