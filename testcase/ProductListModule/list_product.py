'''
@create : lisa
@file :EBST
@Date :2022/2/15
@desc :

'''

# -*- coding:UTF-8 -*-
import unittest,json
import requests
import time,gc
import hashlib
from urllib.parse import urlencode
from public.get_token import Token
from public.get_url import Url
from public.get_headers import Headers

#---------------EBST  商品列表搜索  ----------------------
class product_List(unittest.TestCase):

    def setUp(self):

        # 列表页接口：http: // beta - api.elfbar.com / {name}.html

        self.Url = Url().test_url()+"/coreapi/Elf-Bar_b1900.html"
        print(self.Url)

    def testcase_001(self):
        #获取token
        token = Token().test_token ()
        #获取headers
        headers = Headers().test_get_headers_logined(token)
        # print(token)
        #请求列表接口
        param = {"name": "Elf-Bar_b1900"}
        payload = {"_gid": "GA1.2.474372163.1654678980", "_ga": "GA1.2.2049571130.1654678969",
                   "_ga_8G02ZXM69R": "GS1.1.1654678969.1.1.1654680280.0",
                   "currency_code": "USD", "PHPSESSID": "WBnWTaph261T76cUp8o1h7lajooyNHI8YF2FShos", "R-18": "ebst.com",
                   "product-viewed": "5438",
                   "_atuvc": "1%7C23", "_ga_HE9QE2KCYF": "GS1.1.1654763558.1.1.1654763639.0", "token": token
                   }
        result = requests.get( self.Url, data=payload,headers=headers,params=param)
        result = result.json ()
        print ( result )
        self.assertEqual ( 0, result['code'] )

if __name__ == '__main__':
    unittest.main()