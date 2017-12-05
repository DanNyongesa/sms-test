from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import db
from .database.utils import CRUDMixin
from .utils import kenya_time, slugify


class Topic(db.Model, CRUDMixin):
    """
    :param id: Unique identifier for the message
    :param created_at timestamp fo when the message was created
    """
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime, default=kenya_time)
    slug = Column(String, index=True)
    screens = relationship('Screen', backref='topic', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Topic, self).__init__(**kwargs)
        self.slug = slugify(self.title)

    @staticmethod
    def by_slug(slug):
        topic = Topic.query.filter_by(slug=slug).first_or_404()
        return topic

    @staticmethod
    def by_id(id):
        return Topic.query.get(id)

    def __repr__(self):
        return "<Topic {}>".format(self.id)


class Screen(db.Model, CRUDMixin):
    """Message blob showing on a screen at a given time"""
    __tablename__ = 'screens'
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    timestamp = Column(DateTime, default=kenya_time)
    topic_id = Column(Integer, ForeignKey('topics.id'))

    def __repr__(self):
        return "<Screen index: {0} text: {1}>".format(self.index, self.id)

    def to_dict(self):
        return {
            "text": self.text,
            "index": self.index,
            "message id": self.message_id
        }

    @staticmethod
    def by_id(id):
        return Screen.query.get(id)


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