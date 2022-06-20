# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,os

#---------------获取头值----------------------
class Headers():
    #未登录
    def test_get_headers(self):

        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
                   "Accept": "application/json", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive","Content-Type":"application/json",
}
        return headers


    #已登录
    def test_get_headers_logined(self,token):

        #获取token
        # token = Token().test_token ()
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
                   "Accept": "application/json", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive","cookie":"token="+token,"Content-Type":"application/json",
}
        return headers

