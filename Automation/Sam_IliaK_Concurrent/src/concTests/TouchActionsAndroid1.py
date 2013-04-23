import unittest, time, sys, inspect, datetime
from selenium import webdriver

print "Here are our available touch actions (ignore the ones that look like __xx__): ", dir(webdriver.TouchActions)
#print dir(webdriver)


 
class TouchActionsAndroid1(unittest.TestCase):
    """ Docs: http://selenium.googlecode.com/git/docs/api/py/webdriver/selenium.webdriver.common.desired_capabilities.html
   
    """
    @classmethod
    def setUpClass(self):
        self.name_of_tst=(str(inspect.stack()[0][3]))
 
    def setUp(self):
        #unittest self.id prints out the full test name and file.
        self.name_of_tst = self.id().split('.')[-1]
        self.party_info_dict ={}
        self.run_config= ""
        #self.driver = webdriver.Remote({"browserName":"iexplore", "platform":"WINDOWS"})
        print ("*" * 88)
        
        if len(sys.argv) > 1:
            args = sys.argv
            port = args[1]
            platform = args[2]
            browser = args[3]
            self.run_config= args[4]
            
            #Enable Touch Actions for mobile tests
            if platform=='ANDROID' and browser=='android':
                    
                self.driver = webdriver.Remote(command_executor='http://localhost:8080/wd/hub',  desired_capabilities=webdriver.DesiredCapabilities.ANDROID)
                self.touch =webdriver.TouchActions(self.driver)
            
            else:     
                self.driver = webdriver.Remote("http://localhost:4444/wd/hub",desired_capabilities={
                "browserName": browser,
                "platform": platform,
                "node":port })  
                
        else:
            print "No command line args  passed in. Running regular Webdriver"
            self.driver = webdriver.Firefox()
            #self.driver = webdriver.Ie()
        self.driver.implicitly_wait(7)
        self.now = datetime.datetime.now()
        print ("RUNNING TEST: ",self.name_of_tst," time is:  ", self.now.strftime("%Y-%m-%d %H:%M:%S"))
        self.test_number = 1 # for having different tests continue past fail for data driven tests
        
        driver = self.driver
        print
        
     
        
        #self.driver = webdriver.Firefox()
       

 
    def testHotmailMobile(self):
        self.driver.get("http://www.hotmail.com")
        
        elem=self.driver.find_element_by_css_selector("input[name='login']")
        print "single tap"
        self.touch.tap(elem).perform()
        time.sleep(2)
        elem.send_keys("Hello Matt!")
        time.sleep(2)
        print "double tap"
        self.touch.double_tap(elem).perform()
        time.sleep(2)
        
        #testing that regular webdriver commands still work
        print "Fetching text from the account link: ", self.driver.find_element_by_partial_link_text("Can't access").text
        
        elem= self.driver.find_element_by_css_selector("input[type='submit']")
        self.touch.tap(elem).perform()
        time.sleep(3)
        
    def testByndWeb(self):
        self.driver.get("http://www.bynd.com")
    
        time.sleep(13)   
 
  
    def tearDown(self):
        
        time.sleep(3)
        
        try:
            self.driver.quit()
        except Exception:
            print(" TearDown Method: Browser seems already closed.")

        pass
 
 
def full_suite():

   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(TouchActionsAndroid1))
   return suite

def web_suite():
    #If custom_suite is selected in __main__ it will run the tests below.
    #comment out certain tests to not run them

    suite = unittest.TestSuite()

    suite.addTest(TouchActionsAndroid1('testByndWeb')) 
    #suite.addTest(TouchActionsAndroid1('testGmail')) 


    return suite




def mobile_suite():
    #If custom_suite is selected in __main__ it will run the tests below.
    #comment out certain tests to not run them

    suite = unittest.TestSuite()

    suite.addTest(TouchActionsAndroid1('testHotmailMobile')) 
    #suite.addTest(TouchActionsAndroid1('testGmail')) 


    return suite





if __name__ == '__main__':
  
    runner = unittest.TextTestRunner()
    
    if len(sys.argv) > 1:
        if sys.argv[5]=='full_suite':
            print "Running: ", sys.argv[5]
            print
            runner.run(full_suite())
        
        elif sys.argv[5]=='web_suite':
            print "Running:", sys.argv[5]
            print
            runner.run(web_suite())
        
            
        elif sys.argv[5]=='mobile_suite':
            print "Running:", sys.argv[5]
            print
            runner.run(mobile_suite())
    
    else:
        runner.run(full_suite())
        
