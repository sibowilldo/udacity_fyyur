from .mixins import HasTimestamps
from ..app import db


class Show(HasTimestamps, db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    scheduled_at = db.Column(db.DateTime, nullable=True)
    status_is = db.Column(db.String(50), default='Draft')

    def __repr__(self) -> str:
        return f'<Show {self.id} {self.name} {self.scheduled_at}>'
