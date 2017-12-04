from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship

from .database import db
from .database.utils import CRUDMixin
from .utils import kenya_time


class Message(db.Model, CRUDMixin):
    """
    :param id: Unique identifier for the message
    :param created_at timestamp fo when the message was created
    """
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=kenya_time)
    screens = relationship('Screen', backref='message', lazy='dynamic')

    def __repr__(self):
        return "<Message {}>".format(self.id)


class Screen(db.Model, CRUDMixin):
    """Message blob showing on a screen at a given time"""
    __tablename__ = 'screens'
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    index = Column(Integer, nullable=False, index=True)
    message_id = Column(Integer, ForeignKey('messages.id'))

    def __repr__(self):
        return "<Screen index: {0} text: {1}>".format(self.index, self.id)

    def to_dict(self):
        return {
            "text": self.text,
            "index": self.index,
            "message id": self.message_id
        }


class Feedback(db.Model, CRUDMixin):
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=kenya_time)
    from_ = Column(String(14), nullable=False)
    to_ = Column(String(14), nullable=False)

    def __repr__(self):
        return "<Message {id} {body}>".format(id=self.id, body=self.body)

    def to_dict(self):
        return dict(
            text=self.text,
            created_at=self.timestamp,
            sender=self.from_,
            receipient=self.to_
        )