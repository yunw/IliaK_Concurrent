from selenium import webdriver
import unittest
import sys
import os
from  xmlrunner import *
from utils import DriverFramework
from utils import ReaderFile
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.remote import webelement , command
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions

class GoogleSearch_Page():

    def __init__(self,driver):
      self.driver=driver
      self.touchAction = TouchActions(driver)
             
    def enterSearchKeyword(self, str):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('SearchField')
        self.driver.find_element_by_id(locator).clear()
        self.driver.find_element_by_id(locator).send_keys(str)
        
                                     
    def clickOnSearchButton(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('SearchButton')
        self.driver.find_element_by_name(locator).click()

    def asertTextField(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('SearchField')
        self.assertTrue(self.is_element_present(self.ByLocator(locator)))

    def assertButton(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('SearchButton')
        self.assertTrue(self.is_element_present(By.XPATH, locator))

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def tapOnTextField(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('SearchField')
        element = self.driver.find_element_by_id(locator)
        self.touchAction.tap(element).perform()

    def tapOnSearchButton(self):
        reader = ReaderFile.ReadXML()
        locator = reader.readXml('SearchButton')
        element = self.driver.find_element_by_name(locator)
        self.touchAction.tap(element).perform()

        
    

    def waitTillElementPresent(self,id):
        for i in range(60):
            try:
                if self.is_element_present(By.ID, id): break
            except: pass
            time.sleep(1)
        else: print("unable to find element "+id+" in time")            

        
