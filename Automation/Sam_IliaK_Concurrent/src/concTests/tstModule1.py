'''
Created on 15.09.2011

@author: User
'''
from testconfig import config
from time import sleep

import sys

class testModule_1:
    def test_M1_1(self):
        assert False, "This is a BUG!!!!"
        print 'Module 1 Test 1 Config: ' + config['rc_configuration']['command']
        sleep(1)
    def test_M1_2(self):
        print 'Module 1 Test 2 ' + config['rc_configuration']['command']
        sleep(1)

