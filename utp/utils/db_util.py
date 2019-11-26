import pymysql, redis
from config.setting import mysql_info, redis_info


class Mysql:
    def __init__(self, host, user, password, db, port=3306, charset='utf8'):
        # 构造函数，类在实例化的时候会自动执行构造函数
        self.db_info = {'user': user, 'password': password, "db": db, "port": port, 'charset': charset,
                        'autocommit': True, 'host': host}
        self.__connect()

    def __del__(self):
        self.__close()

    def __connect(self):
        try:
            self.conn = pymysql.connect(**self.db_info)  # 建立连接
        except Exception as e:
            raise Exception("连接不上数据库,请检查数据库连接信息")

        else:
            self.__set_cur()  # 设置游标

    def execute_many(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def execute_one(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    def __set_cur(self, type=pymysql.cursors.DictCursor):  # 设置游标，默认是字典类型
        self.cur = self.conn.cursor(cursor=type)

    def get_list_data(self, sql):
        '''从数据库获取到的数据是list'''
        self.__set_cur(type=None)  # 设置游标为空，返回的就不是字典了
        self.cur.execute(sql)
        self.__set_cur()  # 查完之后重新设置游标为字典类型
        return self.cur.fetchall()

    def __close(self):
        self.conn.close()
        self.cur.close()


def get_redis_connect(name='default'):
    '''获取redis连接，如果不传name，获取默认的链接'''
    redis_config = redis_info.get(name)
    return redis.Redis(**redis_config)


def get_mysql_connect(name='default'):
    '''获取mysql连接，如果不传name，获取默认的链接'''
    mysql_config = mysql_info.get(name)
    return Mysql(**mysql_config)

