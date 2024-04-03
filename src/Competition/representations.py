from ..config import ma
from ..Competition.models import Competition
from marshmallow import validates, ValidationError

class CompetitionSerializer(ma.Schema):
    class Meta:
        model = Competition
        fields = ('id', 'title', 'social_issue', 'user_id', 'user')
