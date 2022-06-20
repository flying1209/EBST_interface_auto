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

#---------------EBST  商品详情页  ----------------------
class goods_products(unittest.TestCase):

    def setUp(self):

        # 文档货品信息接口：http://beta-store.elfbar.com/goods/products
        # 实际地址：GET https://beta-store.elfbar.com/coreapi/goods/products?url=undefined-16365311027836+&goods_id=0

        self.Url = Url().test_url()+"/coreapi/goods/products"
        print(self.Url)

    def testcase_001(self):
        #获取token
        token = Token().test_token ()
        #获取headers
        headers = Headers().test_get_headers_logined(token)

        payload = {"_gid": "GA1.2.474372163.1654678980", "_ga": "GA1.2.2049571130.1654678969",
                   "_ga_8G02ZXM69R": "GS1.1.1654678969.1.1.1654680280.0",
                   "currency_code": "USD", "PHPSESSID": "WBnWTaph261T76cUp8o1h7lajooyNHI8YF2FShos", "R-18": "ebst.com",
                   "product-viewed": "5438",
                   "_atuvc": "1%7C23", "_ga_HE9QE2KCYF": "GS1.1.1654763558.1.1.1654763639.0", "token": token
                   }
        # 请求货品接口
        param = {"url": "undefined-16365311027836",
                 "goods_id": "0"
                 }
        result = requests.get( self.Url, data=payload,headers=headers,params=param)
        result = result.json ()
        print ( result )
        self.assertEqual ( 0, result['code'] )

if __name__ == '__main__':
    unittest.main()