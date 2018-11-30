import os
from app import create_app
from app.extensions import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# 获取config_name
config_name = os.environ.get('FLASK_CONFIG') or 'default'

app = create_app(config_name)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

