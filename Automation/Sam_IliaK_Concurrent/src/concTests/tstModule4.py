
import thread

from time import sleep
#_multiprocess_can_split_ = True
#_multiprocess_shared_ = True
class testModule_4:
    

    #_multiprocess_shared_ = True
    
    #@classmethod
    #def setUpClass(cls):
    #    print 'Module 4 setUpClass'
    
    def someFunc(self):
        print 'bugag'
        

     
    #@classmethod   
    #def tearDownClass(cls):
    #    print 'tearDownClass'
    
    
    def test_M4_1(self):
        print 'Module 4 Test 1' + str(thread.get_ident())
        sleep(1)
        
    
    def test_M4_2(self):
        print 'Module 4 Test 2' + str(thread.get_ident())
        sleep(1)
    
    def test_M4_3(self):
        print 'Module 4 Test 3' + str(thread.get_ident())
        sleep(1)