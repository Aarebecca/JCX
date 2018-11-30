from app.config import config
from flask import Flask
from app.extensions import config_extensions


def create_app(config_name):
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(config[config_name or 'default'])
    config_extensions(app)
    return app
