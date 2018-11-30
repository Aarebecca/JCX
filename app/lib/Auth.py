from app import utils


# 账户管理类
# 每个
class Auth:
    id = ""

    def __init__(self, accesstoken):
        s = utils.SQL()
        sql = ""
