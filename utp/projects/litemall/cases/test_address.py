import unittest
import parameterized
import os
from urllib.parse import urljoin
from projects.litemall.public.const import host, test_user, data_path
from projects.litemall.public import tools
from utils.request import MyRequest
from utils.db_util import get_mysql_connect
from utils.data_util import GetTestData

address_data_path = os.path.join(data_path, 'address.xlsx')  # 拼接测试数据文件的路径
test_address_data = GetTestData.data_for_excel(address_data_path)  # 获取参数化使用的数据


class TestAddress(unittest.TestCase):
    url = urljoin(host, '/wx/address/save')

    @classmethod
    def setUpClass(cls):
        # cls.mysql = get_mysql_connect()  # 获取mysql连接
        token = tools.WxLogin(**test_user).get_token()  # 登录获取token
        cls.header = {'X-Litemall-Token': token}  # 拼header

    @parameterized.parameterized.expand(test_address_data)  # 参数化
    def test_create(self, name, tel, isDefault):
        '''测试添加收货地址'''
        is_default = True if isDefault == '1' else False
        data = {
            "name": name,
            "tel": "%d" % tel,
            "country": "",
            "province": "北京市",
            "city": "市辖区",
            "county": "东城区",
            "areaCode": "110101",
            "postalCode": "",
            "addressDetail": "西二旗",
            "isDefault": is_default
        }
        req = MyRequest(self.url, 'post', data=data, headers=self.header) #发请求
        self.assertEqual(0, req.response.get('errno'), msg='添加失败')#校验错误码是否为0
        address_id = req.response.get('data')
        # sql = 'select name from litemall_address where id = %s;' % address_id
        # db_data = self.mysql.execute_one(sql)
        # self.assertIsNotNone(db_data, msg='litemall:查询地址不存在')#校验是否从数据库查到数据
        # self.assertEqual(db_data.get('name'), name) #判断数据库存的名字和添加的名字是否一样
