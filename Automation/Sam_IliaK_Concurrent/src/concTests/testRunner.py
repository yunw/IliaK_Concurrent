import nose 
from nose.plugins.multiprocess import MultiProcess
import testconfig
from testconfig import TestConfig, config
from nose.plugins.capture import Capture
import sys
from nose.plugins.xunit import Xunit
from ConfigParser import SafeConfigParser



if __name__ == '__main__':
    #nose.main(argv=['nosetests','-s','-v','--processes=10'])
    #nose.main(argv=['nosetests','-s','-v'])
    #nose.run(argv=['nosetests','-v', '--processes=10','--tc-file','config1.ini'], plugins=[MultiProcess(),TestConfig()])
    configFile = sys.argv[1]   
    parser = SafeConfigParser()
    #path_to_project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    parser.read(configFile)
    xunitFile = parser.get('TEST_CONFIG','xunitFile')
    #config['rc_configuration']['command']
    print xunitFile
    nose.run(argv=['nosetests','-v','-s','--with-xunit','--xunit-file='+xunitFile,'--tc-file',configFile], 
             plugins=[TestConfig(),Capture(),Xunit()])
    
    #thread.start_new_thread(nose.run,(['nosetests','-s','--tc-file','config1.ini'],[TestConfig(),Capture()]))   
    #nose.run(argv=['nosetests', '-v','-s', '--processes=10'])
    #testThread('config1.ini').start()
    #testThread('config2.ini').start()
    
    
