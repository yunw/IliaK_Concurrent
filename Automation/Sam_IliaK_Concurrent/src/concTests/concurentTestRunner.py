'''

'''
import subprocess, time

if __name__ == '__main__':

     #p1 = subprocess.Popen('python testRunner.py cfg_FF_ANY_5562.ini')
     #p4 = subprocess.Popen('python testRunner.py cfg_FF_ANY_5562.ini')
     
     #time.sleep(1)
     
     ##Chromedriver 1 not working for some reason. Can try apha version of chromedriver2. (whihc doesnt close at end of run as of 
     ## latest version
     #p2 = subprocess.Popen('python testRunner.py cfg_Chrome_ANY_5563.ini')
     #time.sleep(2)
     # = subprocess.Popen('python testRunner.py cfg_IE_ANY_5560.ini')
     ##p5 WORKS!
     p5 = subprocess.Popen('python testRunner.py cfg_Android_Android_AVD_5554.ini')
     ##p6 WORKS
     #p6 = subprocess.Popen('python testRunner.py cfg_Android_Android_AVD_5556.ini')
     p7 = subprocess.Popen('python testRunner.py cfg_Android_Android_Nexus7_8091.ini')
     
     
#      print 'Process is started'
    
