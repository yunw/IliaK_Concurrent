#import easy to use xml parser called minidom:
from xml.dom.minidom import parseString
from ConfigParser import SafeConfigParser
import os
#all these imports are standard on most modern python implementations
class ReadXML:
    def readXml(self,str):
            #open the xml file for reading:
            file = open("../LocatorFactory/locators.xml",'r')
            #convert to string:
            data = file.read()
            #close file because we dont need it anymore:
            file.close()
            #parse the xml you got from the file
            dom = parseString(data)
            #retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
            xmlTag = dom.getElementsByTagName(str)[0].toxml()
            #strip off the tag (<tag>data</tag>  --->   data):
            xmlData=xmlTag.replace('<'+str+'>','').replace('</'+str+'>','')
            return xmlData
        
    def readInI(self, header,key):
            parser = SafeConfigParser()
            parser.read('../Config/settings.ini')
            value=parser.get(header, key)
            return value