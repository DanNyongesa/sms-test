from flask import render_template, Blueprint, jsonify

callbacks = Blueprint('callbacks', __name__)


@callbacks.route('/sms-notifications')
def sms_notifications():
    """Receives sms callbacks from the user"""

    return jsonify("Hello There"), 200


@callbacks.route('/sms-response')
def sms_response():
    return jsonify("Hello There"), 200