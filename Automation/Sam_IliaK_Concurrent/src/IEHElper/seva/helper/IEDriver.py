'''
Created on Apr 20, 2013

@author: pdam
'''
import unittest
import _winreg as wr
from selenium.webdriver import Ie ,  DesiredCapabilities 
from os import system
from selenium.webdriver.ie.webdriver import WebDriver
from winnt import KEY_WRITE


class Win32Helper(object):
    def __init__(self):
        pass
    
    
    
        
        

    
    def  cleanUpCookiesAndLaunchIE(self):
        caps = DesiredCapabilities.INTERNETEXPLORER
        ie = WebDriver()
        ie.delete_all_cookies()
        ie.get("http://www.yahoo.com")
 
    
    def  cleanUpCache(self  ):
        try:
            system ("RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 255");
        except :
            pass
        
            

       
    
    def disableProtectedMode(self , hostName=None ):
        
        self.regRoot =wr.ConnectRegistry(hostName ,  wr.HKEY_CURRENT_USER )
        
        
        self.strKeyPath =  wr.OpenKeyEx(wr.HKEY_CURRENT_USER ,"Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\1\\")
        try:
            i = 0
            while 1:
                name, value, type = wr.EnumValue(self.strKeyPath, i)
                if name == "2500" :
                    print "%s  :   %s"%(name  ,value)
                    wr.SetValue( self.strKeyPath , name  , wr.REG_SZ , "1"  )
                    wr.FlushKey(self.strKeyPath)
                    wr.CloseKey(self.strKeyPath)  
                    print "%s  :   %s"%(name  ,value)
                i += 1
        except WindowsError:
            print  
        wr.CloseKey(self.strKeyPath)  

        self.strKeyPath =  wr.OpenKeyEx(wr.HKEY_CURRENT_USER ,"Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\2\\")
        try:
            i = 0
            while 1:
                name, value, type = wr.EnumValue(self.strKeyPath, i)
                if name == "2500" :
                    print "%s  :   %s"%(name  ,value)
                    wr.SetValue( self.strKeyPath , name  , wr.REG_SZ , "3"  )
                    wr.FlushKey(self.strKeyPath)
                    wr.CloseKey(self.strKeyPath)  
                    print "%s  :   %s"%(name  ,value)
                i += 1
        except WindowsError:
            print  
        wr.CloseKey(self.strKeyPath) 
        
        
        self.strKeyPath =  wr.OpenKeyEx(wr.HKEY_CURRENT_USER ,"Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\3\\")
        try:
            i = 0
            while 1:
                name, value, type = wr.EnumValue(self.strKeyPath, i)
                if name == "2500" :
                    print "%s  :   %s"%(name  ,value)
                    wr.SetValue( self.strKeyPath , name  , wr.REG_SZ , "3"  )
                    wr.FlushKey(self.strKeyPath)
                    wr.CloseKey(self.strKeyPath)  
                    print "%s  :   %s"%(name  ,value)
                i += 1
        except WindowsError:
            print  
        wr.CloseKey(self.strKeyPath)  
        
        
        self.strKeyPath =  wr.OpenKeyEx(wr.HKEY_CURRENT_USER ,"Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\4\\")
        try:
            i = 0
            while 1:
                name, value, type = wr.EnumValue(self.strKeyPath, i)
                if name == "2500" :
                    print "%s  :   %s"%(name  ,value)
                    wr.SetValue( self.strKeyPath , name  , wr.REG_SZ , "3"  )
                    wr.FlushKey(self.strKeyPath)
                    wr.CloseKey(self.strKeyPath)  
                    print "%s  :   %s"%(name  ,value)
                i += 1
        except WindowsError:
            print  
        wr.CloseKey(self.strKeyPath)  
        
        
         
        
       
       
         
           
    
    def disableZoomIniE(self):  
        regKey = wr.OpenKey(wr.HKEY_CURRENT_USER,"SOFTWARE\\Microsoft\\Internet Explorer\\Zoom")
        try:
            i = 0
            while 1:
                name, value, type = wr.EnumValue(regKey, i)
                if name == "ZoomFactor" :
                    print "%s  :   %s"%(name  ,value)
                    wr.SetValue( regKey , name  , wr.REG_SZ , "100000"  )
                    wr.FlushKey(regKey)
                    wr.CloseKey(regKey)  
                    print "%s  :   %s"%(name  ,value)
                i += 1
        except WindowsError:
            print  
        wr.CloseKey(regKey)  
        
        





class Test(unittest.TestCase):


    def setUp(self):
        w=Win32Helper()
        w.disableZoomIniE()
        w.disableProtectedMode()
        w.cleanUpCache()
        w.cleanUpCookiesAndLaunchIE()
        


    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()