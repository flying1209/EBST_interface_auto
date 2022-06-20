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
class checkout_items(unittest.TestCase):

    def setUp(self):

        # 文档获取待结算货品明细信息（c（checkout）：http://beta-store.elfbar.com/checkout/items
        # 实际地址：https://beta-store.elfbar.com/coreapi/checkout/items

        self.Url = Url().test_url()+"/coreapi/checkout/items"
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
            "is_default": "true",
            "tax_id": "",
            "company_name": "",
            "country": {
                "id": 3273,
                "name": "United States",
                "cn_name": "美国"}}
        coupons = []
        Payload = {
            'address': address,
            'coupons': '' if len(coupons) == 0 else json.dumps(coupons),
            'shipping_method_id':'57'

        }
        result = requests.post(self.Url, data=Payload, headers=headers)
        result=result.json()
        print ( result )
        self.assertEqual ( 0, result['code'] )

if __name__ == '__main__':
    unittest.main()