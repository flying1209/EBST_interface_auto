# -*- coding:UTF-8 -*-
import unittest
import requests
import sys,os


#---------------获取url值----------------------
class Url():

    def test_url(self):

        self.base_url = 'https://beta-store.elfbar.com'
        return self.base_url


    #xls路径
    def test_path(self):
        self.path = 'E:/python35/git/Vaffle/Vaffle_interface/test_date/interface.xls'

        return self.path
