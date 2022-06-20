# -*- coding:UTF-8 -*-
import unittest,json
import requests
import time,gc
import hashlib
from urllib.parse import urlencode
from public.get_url import Url

#---------------获取token值----------------------

class Token():
    def __init__(self):
        self.Url = Url().test_url()+"/coreapi/auth/login"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
                   "Accept": "application/json", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive",}

    #已登录用户获取token
    def test_token(self):
        # 消息体
        payload = {"username": "testing10", "password": "Aa123321", "captcha": "coreapi", }

        result = requests.post ( self.Url, data=payload, headers=self.headers )
        result = result.json ()
        token = result["access_token"]
        print(token)
        return token

