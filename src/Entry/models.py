from ..database import db
from ..User_app.models import BaseModel

class Entry(BaseModel):
    __tablename__ = 'entry'

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(255))
    country = db.Column(db.String(100))
    state = db.Column(db.String(100))
    how_did_you_hear = db.Column(db.String(255))
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'))
    competition = db.relationship('Competition', backref='entries')
    is_entrant_part_of_institution = db.Column(db.Boolean, default=False)
    i_am_part_of = db.Column(db.String(255))

    def __repr__(self):
        return f"<Entry {self.name}>"
