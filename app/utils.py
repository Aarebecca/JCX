import pymysql
import os


class SQL:
    db = None

    def __init__(self):
        import json
        # 读入配置文件
        data = json.load(open(os.path.dirname(__file__)+'/../asset/config.json', 'r'), encoding='UTF-8')["database"]
        self.db = pymysql.connect(data['host'], data['user'], data['password'], data['database'], data['port'])

    def query(self, sql):
        cur = self.db.cursor()
        try:
            cur.execute(sql)
            cur_des = cur.description
            results = cur.fetchall()
            res = []
            for row in results:
                line = {}
                inx = 0
                for col in row:
                    line[cur_des[inx][0]] = col
                    inx = inx + 1
                res.append(line)
            return res
        except Exception as e:
            raise e

    def operator(self, sql):
        cur = self.db.cursor()
        try:
            cur.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()

    def __del__(self):
        self.db.close()
