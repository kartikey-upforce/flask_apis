from flask import jsonify
from marshmallow import ValidationError
from .representations import UserSerializer
from .models import User
from ..database import db


class Users():
    def create_user(self, data):
        serializer = UserSerializer()  
        try:
            validated_data = serializer.load(data)
        except ValidationError as e:
            return jsonify({'error': str(e)}), 400  

        new_user = User(**validated_data)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201
    
    def update_user(self, id, data):
        user = User.query.get(id)
        if user:
            serializer = UserSerializer()
            try:
                validated_data = serializer.load(data)
            except ValidationError as e:
                return jsonify({'error': str(e)}), 400
            
            for attr, value in validated_data.items():
                setattr(user, attr, value)
            
            db.session.commit()
            
            return jsonify({'message': 'User updated successfully'}), 200
        else:
            return jsonify({'error': 'User not found'}), 404

    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'User deleted successfully'}), 200
        else:
            return jsonify({'error': 'User not found'}), 404