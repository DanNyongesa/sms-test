from africastalking.AfricasTalkingGateway import AfricasTalkingGateway

class Flask_AfricasTalkingGateway(AfricasTalkingGateway):
    def __init__(self):
        super(Flask_AfricasTalkingGateway, self).__init__(username=None, apiKey=None, environment='production')

    @classmethod
    def init_app(cls, app):
        cls.username = app.config['AT_USERNAME']
        cls.apiKey = app.config['AT_APIKEY']
        cls.environment = app.config.get('AT_ENVIRONMENT') or 'production'
        cls.Debug = True


AT_gateway = Flask_AfricasTalkingGateway()