import os
import xlrd

from config.setting import log
from .db_util import get_mysql_connect


class GetTestData:
    @staticmethod
    def data_for_txt(file_name):
        '''
        从文本文件里面获取参数化数据
        :param file_name: 文件名
        :return:二维数组
        '''
        log.debug('开始读取参数化文件%s' % file_name)
        if os.path.exists(file_name):
            with open(file_name, encoding='utf-8') as fr:
                data = []
                for line in fr:
                    if line.strip():
                        line_data = line.strip().split(',')
                        data.append(line_data)
            return data
        log.error('%s参数化文件不存在' % file_name)
        raise Exception('%s参数化文件不存在' % file_name)

    @staticmethod
    def data_for_excel(file_name, sheet_name=None):
        '''
        从excel里面读参数化数据
        :param file_name: 文件名
        :param sheet_name: sheet页名字，默认不写取第一个sheet页
        :return: 二维数组
        '''
        log.debug('开始读取参数化文件%s' % file_name)
        if os.path.exists(file_name):
            data = []
            book = xlrd.open_workbook(file_name)
            if sheet_name:
                sheet = book.sheet_by_name(sheet_name)
            else:
                sheet = book.sheet_by_index(0)
            for row_num in range(1, sheet.nrows):
                row_data = sheet.row_values(row_num)
                data.append(row_data)
            return data
        log.error('%s参数化文件不存在' % file_name)
        raise Exception('%s参数化文件不存在' % file_name)

    @staticmethod
    def data_for_mysql(sql, db_config='default'):
        '''
        从数据库里面获取测试数据
        :param sql:sql语句
        :param db_config:从配置文件里面配置的mysql信息
        :return:从数据库里面查出来的二维数组
        '''
        mysql = get_mysql_connect(db_config)
        return mysql.get_list_data(sql)
