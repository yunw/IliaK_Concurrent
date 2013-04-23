from selenium import webdriver
import unittest
import sys
import os
from  xmlrunner import *
from utils import DriverFramework
from utils import ReaderFile
from pageHelper import GoogleSearch_Page
from selenium.webdriver.common.by import By
class GoogleImageSearch(DriverFramework.DriverFramework):
    

    def setUp(self):
        #SUPER::setUp(broswer,platform,port)
        super(GoogleImageSearch,self).setUp(broswer,platform,port)
        
    
    def test_GoogleImageSearch(self):
        reader = ReaderFile.ReadXML()
        helper = GoogleSearch_Page.GoogleSearch_Page(self.driver)
        
        #open application URL
        self.driver.get(reader.readInI('test', "URL"))

        #Assert page title of google page                
        self.assertEqual(self.driver.title, "Google Images")

        #Assert Search field
        locator = reader.readXml('SearchField')
        self.assertTrue(helper.is_element_present(By.ID, locator))
        
        #Enter search string         
        helper.enterSearchKeyword(reader.readInI('test', 'WindowsSearchKeyword'))

        #Assert search button
        locator = reader.readXml('SearchButton');
        self.assertTrue(helper.is_element_present(By.NAME, locator))
        
        #Click on Search button        
        helper.clickOnSearchButton()

        #Assert Result page        
        self.assertEqual(self.driver.title, "weather in san francisco - Google Search")    

    
if __name__ == "__main__":    
    args = sys.argv    
    port  = args[1]
    platform  = args[2]
    broswer = args[3]
    suite = unittest.TestSuite()
    suite.addTest(GoogleImageSearch('test_GoogleImageSearch'))
    runner = XMLTestRunner(file('../Reports/results_test_GoogleImageSearch_%s.xml' % (broswer), "w"))
    runner.run(suite)   