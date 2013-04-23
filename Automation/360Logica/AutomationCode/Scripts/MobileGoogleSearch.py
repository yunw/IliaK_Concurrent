from selenium import webdriver
import unittest, time, re
import sys
import os
from  xmlrunner import *
from utils import DriverFramework
from utils import ReaderFile
from pageHelper import GoogleSearch_Page
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement , command
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions

class MobileGoogleSearch(DriverFramework.DriverFramework):
    

    def setUp(self):
        #SUPER::setUp(broswer,platform,port)
        super(MobileGoogleSearch,self).setUp(broswer,platform,port)
        
    
    def test_MobileGoogleSearch(self):
        reader = ReaderFile.ReadXML()
        helper = GoogleSearch_Page.GoogleSearch_Page(self.driver)
        
        #open application URL
        self.driver.get(reader.readInI('test', "MobileURL"))
        
        #Assert page title of google page                
        self.assertEqual(self.driver.title, "Google")

        #Assert Search field
        locator = reader.readXml('SearchField')
        self.assertTrue(helper.is_element_present(By.ID, locator))
 

        #Enter search string         
        helper.enterSearchKeyword(reader.readInI('test', 'WindowsSearchKeyword'))
        #helper.tapOnTextField()

        #Assert search button
        locator = reader.readXml('SearchButton');
        self.assertTrue(helper.is_element_present(By.NAME, locator))
     
        
        #Click on Search button
        helper.tapOnSearchButton()


        #Assert Result page
        time.sleep(10)
        '''self.assertEqual(self.driver.title, "weather in san francisco - Google Search")
        self.driver.get("http://www.360logica.com/")
        touchactions = TouchActions(self.driver)
        ele= self.driver.find_element_by_link_text("Careers")
        touchactions.tap(ele).perform()
        time.sleep(10)'''


    
if __name__ == "__main__":    
    args = sys.argv    
    port  = args[1]
    platform  = args[2]
    broswer = args[3]
    suite = unittest.TestSuite()
    suite.addTest(MobileGoogleSearch('test_MobileGoogleSearch'))
    runner = XMLTestRunner(file('../Reports/results_test_MobileGoogleSearch_%s.xml' % (broswer), "w"))
    runner.run(suite)   