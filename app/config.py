import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# 配置基类
class Config:
    # 静态文件目录
    STATIC_PATH = os.path.join(BASE_DIR, 'static')
    # 文件上次路径
    UPLOADED_FILES_PATH = os.path.join(BASE_DIR, 'asset/uploads')

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True


class DevelopmentConfig(Config):
    DB_HOST = '127.0.0.1'
    DB_USER = 'root'
    DB_PASSWORD = '123456'
    DB_PORT = '3306'
    DB_DATABASE = 'jcxtest'
    SQLALCHEMY_DATABASE_URI = 'pymysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DATABASE


class TestConfig(Config):
    DB_HOST = '127.0.0.1'
    DB_USER = 'root'
    DB_PASSWORD = '123456'
    DB_PORT = '3306'
    DB_DATABASE = 'jcx'
    'pymysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DATABASE


class ProductionConfig(Config):
    DB_HOST = '127.0.0.1'
    DB_USER = 'root'
    DB_PASSWORD = '123456'
    DB_PORT = '3306'
    DB_DATABASE = 'jcx'
    'pymysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DATABASE


config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}