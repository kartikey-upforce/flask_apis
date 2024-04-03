from flask import jsonify
from marshmallow import ValidationError
from .representations import EntrySerializer
from .models import Entry
from ..database import db


class Entries():
    def create_entry(self, data):
        serializer = EntrySerializer()  
        try:
            validated_data = serializer.load(data)
        except ValidationError as e:
            return jsonify({'error': str(e)}), 400  

        entry = Entry(**validated_data)

        db.session.add(entry)
        db.session.commit()

        return jsonify({'message': 'Entry created successfully'}), 201
    
    def update_entry(self, id, data):
        entry = Entry.query.get(id)
        if entry:
            serializer = EntrySerializer()
            try:
                validated_data = serializer.load(data)
            except ValidationError as e:
                return jsonify({'error': str(e)}), 400
            
            for attr, value in validated_data.items():
                setattr(entry, attr, value)
            
            db.session.commit()
            
            return jsonify({'message': 'Entry updated successfully'}), 200
        else:
            return jsonify({'error': 'Entry not found'}), 404

    def delete_entry(self, entry_id):
        entry = Entry.query.get(entry_id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
            return jsonify({'message': 'Entry deleted successfully'}), 200
        else:
            return jsonify({'error': 'Entry not found'}), 404