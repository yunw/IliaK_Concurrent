# '''
# Created on 15.09.2011
# 
# @author: User
# '''
# from time import sleep
# from testconfig import config
# from selenium import webdriver
# import unittest 
# 
# class testModule_2(unittest.TestCase):
#     global sel
#     sel = None
#     @classmethod
#     def setUpClass(cls):
#         print "Running setup class"
#         self.driver = webdriver.Remote("http://localhost:4444/wd/hub",desired_capabilities={
#                 "browserName": config['rc_configuration']['browser'],
#                 "platform": config['rc_configuration']['platform'],
#                 "node":config['rc_configuration']['node']})  
#                 
#         
#         
# #         global sel
# #         print 'Start Selenium<-------------------------------'
# #         sel = selenium('localhost', 4444, config['rc_configuration']['command'], 'http://workflowy.com')
# #         sel.start()
# #         sel.open('http://workflowy.com', True)    
# 
# 
#         
#     @classmethod
#     def tearDownClass(cls):
#         global sel
#         print 'Stop Selenium<-------------------------------'
#         sel.stop()
#         
#     def test_M2_1(self):
# 
#         print 'Module 2 Test 1 ' + config['rc_configuration']['command']
#         
#         sleep(1)
#     def test_M2_2(self):
#         print 'Module 2 Test 2 ' + config['rc_configuration']['command']
#         sleep(1)
# 
# if __name__ =="__main__":
#     unittest.main()