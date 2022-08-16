from ..app import datetime, db
from sqlalchemy.ext.declarative import declared_attr


class TimestampMixin(object):
    @declared_attr
    def created_at(self):
        return db.Column(db.DateTime, default=datetime.now(), nullable=False)

    @declared_attr
    def updated_at(self):
        return db.Column(db.DateTime, onupdate=datetime.now(), nullable=True)


HasTimestamps = TimestampMixin
