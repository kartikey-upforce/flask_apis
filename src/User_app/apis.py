from flask import request, Blueprint
from .services import Users

user_methods = Users()

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/users', methods=['POST'])
def user_create():
    data = request.json
    return user_methods.create_user(data)
    

@user_blueprint.route('/users/<int:user_id>', methods=['PUT'])
def user_update(user_id):
    data = request.json
    return user_methods.update_user(user_id, data)


@user_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def user_delete(user_id):
    return user_methods.delete_user(user_id = user_id) 
