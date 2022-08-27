from flask import Blueprint, jsonify
from consumer_utils.consumers import Consumer
from algorithms_utils.Mapping import mapping_event
from api.models import Model

model = Model()

consumer = Consumer()

main_api = Blueprint('main_api', __name__)


@main_api.route("/api/v1/state", methods=['GET'])
def mapping_officer():
    consumer.get_msg(mapping_event)
    try:
        incidents = model.get_data("incidents")
        officers = model.get_data("officers")
        return {
            "data": {
                "incidents": incidents,
                "officers": officers
            }
        }
    except Exception as e:
        return jsonify({
            "error": {
                "code": 500,
                "message": "Internal Error"
            }
        })

