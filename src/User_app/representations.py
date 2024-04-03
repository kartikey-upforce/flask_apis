from ..app import ma
from .models import User
from marshmallow import validates, ValidationError


class UserSerializer(ma.Schema):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'gender', 'phone_number')

    @validates('email')
    def validate_email(self, value):
        # Check if email is already present in the database
        existing_user = User.query.filter_by(email=value).first()
        if existing_user:
            raise ValidationError('Email address already exists')

        # Check if email is a valid format
        if '@' not in value or '.' not in value:
            raise ValidationError('Invalid email address')