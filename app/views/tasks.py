from ..celery_cfg import celery
from ..africastalkinggateway import AfricasTalkingGatewayException, AT_gateway as gateway

@celery.task(bind=True, ignore_result=False, countdown=0)
def send_sms(self,message, to_, from_):
    try:
        gateway.sendMessage(to_=to_, from_=from_, message_=message)
    except AfricasTalkingGatewayException as exc:
        raise self.retry(exc=exc, countdown=5)