from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

class Flask_AfricasTalkingGateway(AfricasTalkingGateway):
    def __init__(self):
        super(Flask_AfricasTalkingGateway, self).__init__(username=None, apiKey=None, environment='production')

    def init_app(self, app):
        self.username = app.config['AT_USERNAME']
        self.apiKey = app.config['AT_APIKEY']
        self.environment = app.config.get('AT_ENVIRONMENT') or 'production'
        self.Debug = True


AT_gateway = Flask_AfricasTalkingGateway()