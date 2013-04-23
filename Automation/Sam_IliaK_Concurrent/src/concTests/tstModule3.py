'''
Created on 15.09.2011

@author: User
'''
from time import sleep
import thread

class testModule_1:
    def test_M3_1(self):
        print 'Module 3 Test 1 '
        sleep(2)
    def test_M3_2(self):
        print 'Module 3 Test 2 '
        sleep(2)
    
    def test_M3_3(self):
        print 'Module 3 Test 3 ' + str(thread.get_ident())
        sleep(2)
        
    def test_M3_4(self):
        assert False
        print 'Module 3 Test 4 ' + str(thread.get_ident())
        sleep(2)
    
    def test_M3_5(self):
        print 'Module 3 Test 5 ' + str(thread.get_ident())
        sleep(2)
