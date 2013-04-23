'''
Created on 15.09.2011

@author: User
'''
from time import sleep
from testconfig import config
from selenium.selenium import selenium

class testModule_2:
    global sel
    sel = None
    @classmethod
    def setUpClass(cls):
        global sel
        print 'Start Selenium<-------------------------------'
        sel = selenium('localhost', 4444, config['rc_configuration']['command'], 'http://workflowy.com')
        sel.start()
        sel.open('http://workflowy.com', True)
        
    @classmethod
    def tearDownClass(cls):
        global sel
        print 'Stop Selenium<-------------------------------'
        sel.stop()
        
    def test_M2_1(self):

        print 'Module 2 Test 1 ' + config['rc_configuration']['command']
        
        sleep(1)
    def test_M2_2(self):
        print 'Module 2 Test 2 ' + config['rc_configuration']['command']
        sleep(1)
