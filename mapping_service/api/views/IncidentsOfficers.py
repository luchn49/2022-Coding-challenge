from flask import Blueprint, jsonify

main_api = Blueprint('main_api', __name__)

@main_api.route("/api/incidents_Officer", methods=['GET'])
def mapping_officer():
    pass

