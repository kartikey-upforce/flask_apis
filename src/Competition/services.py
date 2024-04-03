from flask import jsonify
from marshmallow import ValidationError
from .representations import CompetitionSerializer
from .models import Competition
from ..database import db


class Competitions():
    def create_competition(self, data):
        serializer = CompetitionSerializer()  
        try:
            validated_data = serializer.load(data)
        except ValidationError as e:
            return jsonify({'error': str(e)}), 400  

        competition = Competition(**validated_data)

        db.session.add(competition)
        db.session.commit()

        return jsonify({'message': 'Competition created successfully'}), 201
    
    def update_competition(self, id, data):
        competition = Competition.query.get(id)
        if competition:
            serializer = CompetitionSerializer()
            try:
                validated_data = serializer.load(data)
            except ValidationError as e:
                return jsonify({'error': str(e)}), 400
            
            for attr, value in validated_data.items():
                setattr(competition, attr, value)
            
            db.session.commit()
            
            return jsonify({'message': 'Competition updated successfully'}), 200
        else:
            return jsonify({'error': 'Competition not found'}), 404

    def delete_competition(self, competition_id):
        competition = Competition.query.get(competition_id)
        if competition:
            db.session.delete(competition)
            db.session.commit()
            return jsonify({'message': 'Competition deleted successfully'}), 200
        else:
            return jsonify({'error': 'Competition not found'}), 404