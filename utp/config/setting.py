import os
import nnlog

mysql_info = {
    'default':
        {
            'host': 'ip',
            'port': 3306,
            'user': 'dbuser',
            'password': 'dbpassword',
            'db': 'db',
            'charset': 'utf8',
        }
} #数据库配置，多个数据库，在字典里加key就可以了

redis_info = {
    'default': {
        'host': 'ip',
        'port': 6379,
        'db': 0,
        'decode_responses': True
    }
}#redis配置，多个数据库，在字典里加key就可以了

email_info = {
    'host': 'smtp.163.com',  #
    'user': 'user@163.com',  # 用户
    'password': 'password',  # 密码
    'port': 465,
}

email_to = ['niuhanyang@163.com', '2273747892@qq.com', '243551032@qq.com', '511402865@qq.com']
email_cc = ['1064393357@qq.com', '382706058@qq.com']

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = os.path.join(base_path, 'logs', 'utp.log')  # 指定日志文件
projects_path = os.path.join(base_path, 'projects')  # 项目目录
log = nnlog.Logger(log_path)

email_template = '''
各位好：
    本次接口测试结果如下：总共运行{all_count}条用例，通过{pass_count}条，失败【{fail_count}】条。
    详细信息请查看附件。
'''#邮件模板
