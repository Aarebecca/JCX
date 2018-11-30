from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate(db)


def config_extensions(app):
    db.init_app(app)
    migrate.init_app(app)
