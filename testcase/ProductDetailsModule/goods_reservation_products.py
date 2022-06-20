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
class good_reservation_products(unittest.TestCase):

    def setUp(self):

        # 文档相关接口：http://beta-api.elfbar.com/member/reservation-products

        # 实际地址：https://beta-store.elfbar.com/coreapi/member/reservation-products

        self.Url = Url().test_url()+"/coreapi/member/reservation-products"
        print(self.Url)

    def testcase_001(self):
        #获取token
        token = Token().test_token ()
        #获取headers
        headers = Headers().test_get_headers_logined(token)
        # print(token)
        items = [{"product_bn":"EB2021111006",
                  "quantity": 2}]
        payload = {"items":items}

        # payload = {"items[0][product_bn]": "11010433145000", "items[0][quantity]": "1"}
        print(payload)

        result = requests.post( self.Url, data=json.dumps(payload),headers=headers)
        result = result.json ()
        print ( result )
        self.assertEqual ( 0, result['code'] )

if __name__ == '__main__':
    unittest.main()