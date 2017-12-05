from app import redis
import json
from .tasks import send_sms

from ..models import Topic


def respond(text, to_, from_):
    session = redis.get(to_)
    if session is None or text is None:
        topics = Topic.query.all()
        message = ''
        c_msg = {}
        for index, topic in enumerate(topics):
            index += 1
            message = "{message}\n{index}.{text}".format(message=message, index=index, text=topic.title)
            c_msg[str(index)] = topic.id
        redis.set(to_, json.dumps({'topics': c_msg, 'home': 1}))
        message = 'Welcome to Doodore SMS Training. Kindly select a Topic to proceed{}'.format(message)
        send_sms.apply_async(kwargs={'message': message, "to_": to_, "from_": from_})
        return False

    session = json.loads(session.decode())
    if session['home']:
        session['home'] = None
        topic_id = session['topics'].get(text)
        topic = Topic.by_id(topic_id)

        if topic is None:
            send_sms.apply_async(kwargs={'message': "Inavalid Input", "to_": to_, "from_": from_})
            return False

        session['selected_topic'] = topic.id
        session['index'] = 0
    else:
        topic = Topic.by_id(session['selected_topic'])
        if topic is None:
            send_sms.apply_async(kwargs={'message': "Inavalid Input", "to_": to_, "from_": from_})
            return False

    while topic.screens.count() > session['index']:
        screen = topic.screens[session['index']]
        text = screen.text
        message = '{}\n(1.More)'.format(text)
        session['index'] += 1
        redis.set(to_, json.dumps(session))
        break
    else:
        message = "You have reached the end"
        redis.delete(to_)


    send_sms.apply_async(kwargs={'message': message, "to_": to_, "from_": from_})
