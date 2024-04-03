from ..config import ma
from ..Entry.models import Entry
from marshmallow import validates, ValidationError

class EntrySerializer(ma.Schema):
    class Meta:
        model = Entry
        fields = ('id', 'name', 'country', 'state', 'how_did_you_hear', 'competition_id','competition', 'is_entrant_part_of_institution', 'i_am_part_of')
