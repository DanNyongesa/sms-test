from sqlalchemy import Column, Integer, String, DateTime, Text
from .database import db
from .database.utils import CRUDMixin


class Message(db.Model, CRUDMixin):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    body = Column(Text, nullable=False)
    timestamp = Column(DateTime)
    from_ = Column(String(14), nullable=False)
    to_ = Column(String(14), nullable=False)

    def __repr__(self):
        return "<Message {id} {body}>".format(id=self.id, body=self.body)

    def to_dict(self):
        return dict(
            body=self.body,
            created_at=self.timestamp,
            sender=self.from_,
            receipient=self.to_
        )