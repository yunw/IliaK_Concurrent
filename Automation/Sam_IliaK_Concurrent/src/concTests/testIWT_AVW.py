from include import *
from testconfig import config

file_name = os.path.relpath(__file__)[:-3]


class testIWT_AVW(unittest.TestCase):
 
    #capabilities = None
    
    
    
    @classmethod
    def setUpClass(self):
        ## Do One time DB modifies etc here, as long as they dont mess with concurrency
        self.name_of_tst=(str(inspect.stack()[0][3]))
        self.verificationErrors = []
        self.dirty_data=[]
        self.base_url = "http://"
        
        self.iwt_tst_helper = SeleniumTestHelper.IWTtestHelperTwo()
        self.sel_helper =SeleniumTestHelper.SeleniumTestHelperTwo()
        
        
        self.username = "ssaftest"
        self.lastName = "intraxSaf"
        self.dateTime=datetime.datetime.now().strftime("%Y%m%d%H%M")
        self.Season = "Spring 2013" # "Summer 2013"  "Winter 2013"
        self.country= "Thailand"   # Summer (may and june)>> Bulgaria # Winter (nov and dec)>>Brazil # Spring(mar and apr) >> Thailand 
        self.SeasonId = "16"  #Spring 2013.   select top 100* from ICDSeason
        #season start date will be X days before today
        self.season_start_date = datetime.datetime.now()- datetime.timedelta(days=21) #).strftime("%d.%m.%Y")
        self.season_end_date = datetime.datetime.now() + datetime.timedelta(days=30)  #).strftime("%d.%m.%Y")
        self.pax_start_date = self.season_start_date + datetime.timedelta(days=1)
        #Season start date for country modify via sql

        print
            
#     def __init__(self, browser="firefox",browser1="firefox1", platform="WINDOWS", browser2="firefox2"):
#          
#         self.capabilities= {"browserName":browser, "platform":platform}
#         self.driver= webdriver.Remote("http://localhost:5555/wd/hub", self.capabilities) 
#         #print "Inited SeleniumTestHelperTwo!!"
#         pass
    
    def setUp(self):
        #unittest id prints out the full test name and file.
        self.name_of_tst = self.id().split('.')[-1]
        self.party_info_dict ={}
        
        
        if config['rc_configuration']['platform']=='ANDROID':
            #executor= 'http://'+'localhost:'+config['rc_configuration']['hostport']+'/wd/hub'
            #print executor

            hostport=config['rc_configuration']['hostport']
            self.driver = webdriver.Remote(command_executor='http://localhost:'+str(hostport)+'/wd/hub',  desired_capabilities=webdriver.DesiredCapabilities.ANDROID)
            self.touch =webdriver.TouchActions(self.driver)#                                            desired_capabilities={
            self.driver.implicitly_wait(20)
       
        
        else:
            self.driver = webdriver.Remote("http://localhost:4444/wd/hub",desired_capabilities={
                "browserName": config['rc_configuration']['browser'],
                "platform": config['rc_configuration']['platform'],
                "node":config['rc_configuration']['node']})  
                
        
        
        #self.driver = webdriver.Firefox()
        #self.driver   = webdriver.Ie()
        
# # # #         print Helper
        self.now = datetime.datetime.now()
        print (self.name_of_tst," time is:  ", self.now.strftime("%Y-%m-%d %H:%M:%S"))
        self.test_number = 1 # for having different tests continue past fail for data driven tests
        
        driver = self.driver
        print
    
    
        
    
    
    def tst_bynd1(self, rand_avw_addr="random"):
        try:
            """ not finished as test is waiting for address update to work on Qa1
            This will fail until we remove the AVW from international address. 
            Then it may fail due to StateDtl.Abbr not being international?! 
            Or that DB query and assertions are still from older versions
             """
            driver = self.driver
            self.party_info_dict ={"sk8723_can@yahoo.co.jpx":"1031184"}
            
            # Login to Pluto
                       
            for party_email, party_id in self.party_info_dict.items():
                
                #driver.get(self.base_url + 'www.hotmail.com')  
                driver.get(self.base_url + 'www.bynd.com')  
                
                print "Fetching text from article post: ", self.driver.find_element_by_css_selector("span.f-os.f-14").text
#                 elem= self.driver.find_element_by_css_selector("span.f-os.f-14")
#                 self.touch.tap(elem).perform()
#                 time.sleep(3)
#                 
#                 driver.get(self.base_url + config.INTRAX + "/icd/participant/viewICDParticipantAddresses.action?icdParticipantId=%s" % party_id)
                time.sleep(4)
                print ("Test done! :D") 
                
        except Exception as e:
            eval_exception_result = eval(SeleniumTestHelper.exception_result)
            print eval_exception_result
            self.fail(eval_exception_result)              

    def test_photoswipe1(self, rand_avw_addr="random"):
        try:
            """ not finished as test is waiting for address update to work on Qa1
            This will fail until we remove the AVW from international address. 
            Then it may fail due to StateDtl.Abbr not being international?! 
            Or that DB query and assertions are still from older versions
             """
            driver = self.driver
            self.party_info_dict ={"sk87xxxxxxxx1@yahoo.co.jpx":"1031184"}
            
            # Login to Pluto
                       
            for party_email, party_id in self.party_info_dict.items():
                
                #driver.get(self.base_url + 'www.hotmail.com')  
        
                
                driver.get("http://www.photoswipe.com/latest/examples/04-jquery-mobile.html")
                driver.find_element_by_link_text("First Gallery").click()
                elem =driver.find_element_by_css_selector("img[alt=\"Image 001\"]")
                self.touch.tap(elem).perform()
                elem =driver.find_element_by_css_selector("div.ps-uilayer")
                time.sleep(3)
                ##Failing here.
                self.touch.flick_element(elem,-350, 0, 1).perform()
                time.sleep(3)
                #flick_element(self, on_element, -400, 0, speed_pixels_ps):
                
#                 elem= self.driver.find_element_by_css_selector("span.f-os.f-14")
#                 self.touch.tap(elem).perform()
#                 time.sleep(3)
#                 
#                 driver.get(self.base_url + config.INTRAX + "/icd/participant/viewICDParticipantAddresses.action?icdParticipantId=%s" % party_id)
                time.sleep(4)
                print ("Test done! :D") 
                
        except Exception as e:
            eval_exception_result = eval(SeleniumTestHelper.exception_result)
            print eval_exception_result
            self.fail(eval_exception_result)              


    
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert.text
        finally: self.accept_next_alert = True 
    
    def tearDown(self):
        time.sleep(3)
        
        try:
            self.driver.quit()
        except Exception:
            print(" TearDown Method: Browser seems already closed.")

        pass
        
        
    @classmethod
    def tearDownClass(self):
        time.sleep(0)
        print
        print("Running: ",(inspect.stack()[0][3]))
        print ("This data needs investigation/cleanup: ",self.dirty_data)
        #self.assertEqual([], self.verificationErrors)
        #print ("Failures: ",self.verificationErrors)
        
#        try:
#            self.driver.quit()
#            
#        except Exception:
#            print("Closing Webdriver in TearDown Class")
#            pass




    def tearDown(self):
        time.sleep(3)
        
        try:
            self.driver.quit()
        except Exception:
            print(" TearDown Method: Browser seems already closed.")
 
        pass
        
        
    @classmethod
    def tearDownClass(self):
        time.sleep(0)
        print
        print("Running: ",(inspect.stack()[0][3]))
        print ("This data needs investigation/cleanup: ",self.dirty_data)
        #self.assertEqual([], self.verificationErrors)
        #print ("Failures: ",self.verificationErrors)
        
#        try:
#            self.driver.quit()
#            
#        except Exception:
#            print("Closing Webdriver in TearDown Class")
#            pass


def full_suite():

   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(testIWT_AVW))
   return suite


def custom_suite():
    
    #If custom_suite is selected in __main__ it will run the tests below.
    #comment out certain tests to not run them

    suite = unittest.TestSuite()
    
#     suite.addTest(IWT_AVW('test_pluto_avw_pax_address')) 
    #suite.addTest(testIWT_AVW('test_bynd1'))
    suite.addTest(testIWT_AVW('test_photoswipe1'))
    return suite





if __name__ == '__main__':
  
    runner = unittest.TextTestRunner()
    runner.run(custom_suite())
    
    
#     if len(sys.argv) > 1:
#         if sys.argv[5]=='full_suite':
#             print "Running: ", sys.argv[5]
#             print
#             runner.run(full_suite())
#             
#         elif sys.argv[5]=='custom_suite':
#             print "Running:", sys.argv[5]
#             print
#             runner.run(custom_suite())
#     
#     else:
#         runner.run(custom_suite())
        

    #unittest.main()
    
    
    
    #getting into my car. guy comes up can u help me out. Points
