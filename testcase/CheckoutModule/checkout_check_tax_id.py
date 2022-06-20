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
class checkout_check_tax_id(unittest.TestCase):

    def setUp(self):

        # 文档检查是否需要税号（tax id）：http://beta-store.elfbar.com/checkout/check-tax-id-need
        # 实际地址：https://beta-store.elfbar.com/coreapi//checkout/check-tax-id-need?country_id=3273&shipping_method_id=7
        # 目前有印度 + DHL / UPS / FEDEX ，美国 + UPS(id95)这几种组合条件需要做这个检查

        self.Url = Url().test_url()+"/coreapi/checkout/check-tax-id-need"
        print(self.Url)

    def testcase_001(self):
        #获取token
        token = Token().test_token ()
        #获取headers
        headers = Headers().test_get_headers_logined(token)
        Payload = {"_gid": "GA1.2.474372163.1654678980", "_ga": "GA1.2.2049571130.1654678969",
                   "_ga_8G02ZXM69R": "GS1.1.1654678969.1.1.1654680280.0",
                   "currency_code": "USD", "PHPSESSID": "WBnWTaph261T76cUp8o1h7lajooyNHI8YF2FShos", "R-18": "ebst.com",
                   "product-viewed": "5438",
                   "_atuvc": "1%7C23", "_ga_HE9QE2KCYF": "GS1.1.1654763558.1.1.1654763639.0", "token": token
                   }
        param={"country_id":3273,"shipping_method_id":95}
        result = requests.get(self.Url, data=Payload, headers=headers,params=param)
        result=result.json()
        print ( result )
        self.assertEqual ( 0, result['code'] )

if __name__ == '__main__':
    unittest.main()