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

#---------------EBST 结算页 ----------------------
class checkout_create_order(unittest.TestCase):

    def setUp(self):

        # 文档提交订单（checkout）：http://beta-store.elfbar.com/checkout/create-order
        # 实际地址：https://beta-store.elfbar.com/coreapi/checkout/create-order

        self.Url = Url().test_url()+"/coreapi/checkout/create-order"
        print(self.Url)

    def testcase_001(self):
        #获取token
        token = Token().test_token ()
        #获取headers
        headers = Headers().test_get_headers_logined(token)

        address = {
            "id": 176509,
            "consignee": "test ning",
            "country_id": 3273,
            "province_id": 1,
            "province": "Alabama",
            "city": "shanghai",
            "street": "huaer street",
            "post_code": "200000",
            "phone": "10086",
            "is_default": "false",
            "tax_id": "",
            "company_name": "",
            "country": {
                     "id": 3273,
                     "name": "United States",
                     "cn_name": "美国"}
            }
        Payload = {
            "address": address,
            "payment_method_id": 77,
            "shipping_method_id": 75,
            "order_note": "test order api",
            "coupons": [],
        }
        result = requests.post(self.Url, data=json.dumps(Payload), headers=headers)
        result=result.json()
        print ( result )
        self.assertEqual ( 0, result['code'])

if __name__ == '__main__':
    unittest.main()