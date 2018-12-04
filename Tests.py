'''
Created on 9 lis 2018

@author: ewelina
'''
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(); 
#         add a bug
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        
