from ..database import db
from ..User_app.models import BaseModel

class Competition(BaseModel):
    __tablename__ = 'competition'

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    title = db.Column(db.String(255))
    social_issue = db.Column(db.ARRAY(db.String(255)))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='competitions')

    def __repr__(self):
        return f"<Competition {self.title}>"
