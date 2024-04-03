from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
# from database import db
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/test_db"

db.init_app(flask_app)
migrate = Migrate(flask_app, db)
ma = Marshmallow(flask_app)

from .User_app.apis import user_blueprint
from .Competition.apis import competition_blueprint
from .Entry.apis import entry_blueprint

flask_app.register_blueprint(user_blueprint)
flask_app.register_blueprint(competition_blueprint)
flask_app.register_blueprint(entry_blueprint)

def run_app():
    with flask_app.app_context():
        db.create_all()
        os.system('flask db upgrade')

    from User_app.apis import user_blueprint
    from Competition.apis import competition_blueprint
    from Entry.apis import entry_blueprint

    flask_app.register_blueprint(user_blueprint)
    flask_app.register_blueprint(competition_blueprint)
    flask_app.register_blueprint(entry_blueprint)

    flask_app.run(debug=True)



if __name__ == '__main__':
    run_app()
