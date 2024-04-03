from flask import Blueprint, request, jsonify
from .services import Entries

entry_blueprint = Blueprint('entry', __name__)

entry_methods = Entries()

@entry_blueprint.route('/entry', methods=['POST'])
def entry_create():
    data = request.json
    return entry_methods.create_entry(data)
    

@entry_blueprint.route('/entry/<int:entry_id>', methods=['PUT'])
def entry_update(entry_id):
    data = request.json
    return entry_methods.update_entry(entry_id, data)


@entry_blueprint.route('/entry/<int:entry_id>', methods=['DELETE'])
def entry_delete(entry_id):
    return entry_methods.delete_entry(entry_id = entry_id) 