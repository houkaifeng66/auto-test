
import pymysql
from utils.config_util import config
from pymysql.cursors import DictCursor

class DBHandler:
    def __init__(self):
        db_conf = config.get("db_config")
        # 这里填入你 litemall 数据库的配置
        self.conn = pymysql.connect(
            host=db_conf['host'],
            port=db_conf['port'],
            user=db_conf['user'],
            password=db_conf['password'],
            database=db_conf['database'],
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()

    def query_one(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()