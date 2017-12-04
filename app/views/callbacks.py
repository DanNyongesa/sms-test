from flask import current_app as app

from dateutil import parser
from flask import Blueprint, jsonify, request

from ..models import Feedback
from .utils import respond

callbacks = Blueprint('callbacks', __name__)

@callbacks.route('/sms/incoming-message', methods=['post', 'get'])
def sms_incoming_message():
    """Receives sms callbacks from the user & saves message to the database
    :param from: The number that sent the message
    :param to: The number to which the message was sent
    :param text: The message content
    :param date: The date and time when the message was received
    :param id: The internal ID that we use to store this message
    :param linkId: Optional parameter required when responding to an on-demand user request with a premium message
    """
    from_ = request.values.get('from')
    to_ = request.values.get('to')
    text = request.values.get('text')
    timestamp = parser.parse(request.values.get('date'))
    id_ = request.values.get('id')
    linkId = request.values.get('linkId')
    app.logger.info(
        "{id} [from: {0} to: {1}] body: {2} [{timestamp}]".format(to_, from_, text, timestamp=timestamp, id=id_))
    # record message
    message = Feedback.create(to_=to_, from_=from_, text=text, timestamp=timestamp)

    # send response
    if text == '':
        text = None
    respond(to_=from_, from_=to_, text=text)

    return jsonify('Received Message'), 200


@callbacks.route('/sms/delivery-report', methods=['post', 'get'])
def sms_delivery_report():
    return jsonify("Hello There"), 200


@callbacks.route('/sms/subscription-notifications', methods=['post', 'get'])
def sms_subscription_notification():
    return jsonify("Hello There"), 200


@callbacks.route('/sms/sms-opt-out', methods=['post', 'get'])
def sms_opt_out():
    return jsonify("H   ello There"), 200
