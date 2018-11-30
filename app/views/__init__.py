from .info import info
from .files import files
from .main import main

DEFAULT_BLUEPRINT = (
    (info, '/info'),
    (files, '/files'),
    (main, '/')
)


# 封装配置蓝本的函数
def config_blueprint(app):
    # 循环读取元组中的蓝本
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(
            blueprint,
            url_prefix=prefix,
            static_folder='static/'
        )
