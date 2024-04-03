from flask import Blueprint, request, jsonify
from .services import Competitions

competition_blueprint = Blueprint('competition', __name__)

competition_methods = Competitions()

@competition_blueprint.route('/competition', methods=['POST'])
def competition_create():
    data = request.json
    return competition_methods.create_competition(data)
    

@competition_blueprint.route('/competition/<int:competition_id>', methods=['PUT'])
def competition_update(competition_id):
    data = request.json
    return competition_methods.update_competition(competition_id, data)


@competition_blueprint.route('/competition/<int:competition_id>', methods=['DELETE'])
def competition_delete(competition_id):
    return competition_methods.delete_competition(competition_id = competition_id) 