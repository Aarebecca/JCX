from app.extensions import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'User'
    # 账号
    id = db.Column(db.String(32), primary_key=True, nullable=False, index=True)
    # 昵称
    nickname = db.Column(db.String(45), default="未设置昵称")
    # 密码 这里的密码使用RSA加密
    password = db.Column(db.String(256), nullable=False)
    # 注册时间
    signin_time = db.Column(db.DateTime, default=datetime.now())
    # 用户权限
    authority = db.Column(db.String(16), nullable=False, default="default")
    # 用户身份
    identity = db.Column(db.String(16), nullable=False, default="default")

    def __repr__(self):
        return self.id[:20]
