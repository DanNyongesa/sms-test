from app import redis
import json
from .tasks import send_sms

Screens = [
    {
        'text': 'Farming is growing crops or keeping animals by people for food and raw materials. '
                'Farming is a part of agriculture.',
        'index': 0,
        'message_id': 1
    },
    {
        'text': 'Agriculture started thousands of years ago, but no one knows for sure how old it is.[1] '
                'The development of farming gave rise to the Neolithic Revolution whereby people gave up nomadic '
                'hunting and became settlers in what became cities.',
        'index': 2,
        'message_id': 1
    },
    {
        'text': 'Agriculture and domestication probably started in the Fertile Crescent '
                '(the Nile Valley, The Levant and Mesopotamia).[2] The area called Fertile '
                'Crescent is now in the countries of Iraq, Syria, Turkey, Jordan, Lebanon, Israel, and Egypt. '
                'Wheat and barley are some of the first crops people grew. '
                'People probably started agriculture slowly by planting a few crops, '
                'but still gathered many foods from the wild.',
        'index': 3,
        'message_id': 1
    }
]

Message = {
    'id': 1,
    'name': 'Introduction to Farming',
    'screens': Screens
}


def respond(text, to_, from_):
    session = redis.get(to_)
    if session is None or text is None:
        message = Message['name']
        screens = Message['screens']
        redis.set(to_, json.dumps({'screens': screens, 'index':0}))
        message = 'Welcome to Doodore SMS Training. Kindly select a Topic to proceed\n' \
                  '1.{}'.format(message)

    else:
        session = json.loads(session.decode())
        msg_screens = session.get('screens')
        print(msg_screens)
        print(session.get('index'))
        screens = list(filter(lambda screen: screen['index']==session.get('index', 0), msg_screens))
        if screens:
            message = screens[0]['text']
        else:
            message = 'End'
        index = session.get('index', 0)
        while len(Screens) > index:
            message = '{}\n(1.More)'.format(message)
            session['index'] += 1
            redis.set(to_, json.dumps(session))
            break
        else:
            redis.delete(to_)


    send_sms.apply_async(kwargs={'message': message, "to_": to_, "from_": from_})
