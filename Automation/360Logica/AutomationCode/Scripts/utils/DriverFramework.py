
from selenium import webdriver
import unittest
import sys
import os
from  xmlrunner import *
from utils import ReaderFile
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
class DriverFramework(unittest.TestCase):
    
    capabilities = None
    
    def setUp(self,broswer,platform,port):
        
        reader = ReaderFile.ReadXML()
        runMode=reader.readInI('test', "RunMode")
        hubIP=reader.readInI('server', "hub_IP")
        hubPort=reader.readInI('server', "hub_Port")
        executor= 'http://'+hubIP+':'+hubPort+'/wd/hub'
        if(runMode=='Windows'):            
            if (broswer=='iehta'):
                self.driver = webdriver.Remote(command_executor=executor,desired_capabilities={
                "browserName": broswer,
                "node": port,
                "platform": platform,
                "javascriptEnabled": True,})
                
            if (broswer=='chrome'):
                self.driver = webdriver.Remote(command_executor=executor,desired_capabilities={
                "browserName": broswer,
                "node": port,
                "platform": platform,
                "javascriptEnabled": True,})
                
            if (broswer=='firefox'):  
                self.driver = webdriver.Remote(command_executor=executor,desired_capabilities=DesiredCapabilities.FIREFOX)

        if(runMode=='Android'):
            self.driver = webdriver.Remote(command_executor=executor,desired_capabilities={
                "browserName": broswer,
                "node": port,
                "platform": platform,
                "javascriptEnabled": True,})
            self.driver.implicitly_wait(45)

        if(runMode=='iOS'):
            self.driver = webdriver.Remote(command_executor='http://'+hubIP+':3001/wd/hub',desired_capabilities={
            "browserName": broswer,
            "node": port,
            "platform": platform,
            "javascriptEnabled": True,})

              
    def tearDown(self):
        self.driver.quit()

    
