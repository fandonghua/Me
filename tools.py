import pymysql,hashlib

def op_mysql(sql,many=True):
    db_info = {'user': 'jxz', 'password': '123456',
            'host': '118.24.3.40', 'db': 'jxz', 'port': 3306, 'charset': 'utf8',
            'autocommit': True}
    conn = pymysql.connect(**db_info)  # 建立连接
    cur = conn.cursor(pymysql.cursors.DictCursor)  # 游标
    cur.execute(sql)  # 执行sql语句，insert 、update 、delete
    if many:
        result = cur.fetchall()
    else:
        result = cur.fetchone() # {''}
    cur.close()
    conn.close()
    return result

def md5(s,salt=''):
    new_s = str(s) + salt
    m = hashlib.md5(new_s.encode())
    return m.hexdigest()