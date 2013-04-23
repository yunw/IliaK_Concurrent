import unittest, inspect, datetime, sys, os, csv,time, re, traceback, random
import argparse, optparse, pyodbc, pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException 

## TO DO:
## Move and comment stuff out of the non instantiatable classes into IWT_Two Selenium_Two etc

env_variable="qa1"  #available options: "developer", "dev", "qa1","qa2", "stage"
base_url = "http://"

exception_result = """SeleniumTestHelper.SeleniumTestHelperTwo.exception_found\
(e,traceback.format_exc(), self.now, file_name, self.name_of_tst, self.driver\
                        ,[self.party_info_dict], self.test_number)"""

#capabilities= {"browserName":"firefox", "platform":"WINDOWS"}

                        
class SeleniumTestHelperTwo(unittest.TestCase):
    
    
    printer = "Printer!!"
    def __init__(self):

        #print "Inited SeleniumTestHelperTwo!!"
        pass
    
    
    @classmethod
    def environment_setter(self, option):
        
        if option == 'developer':
            print "running tests for: Developer_Machine"
            import VariablesDEVELOPER_Machine_WD as config
            
        elif option == 'dev':
            print "running tests for: DEV"
            import VariablesDEV_WD as config
            
        elif option == "qa1":
            print "running tests for: QA1"
            import VariablesQA1_WD as config
        
        elif option == "qa2":
            print "running tests for: QA2"
            import VariablesQA2_WD as config
            
        elif option == "stage":
            print "running tests for: STAGE"
            import VariablesSTAGE_WD as config 
            
        elif option == "prod":
            print "You are running the test in Prod. This is not allowed"
        """ locals() return everything in my namespace, but we used config """   
        return config
        
    @classmethod
    def pickle_data(self, some_dict, pickled_file):
        data = {}
        if os.path.isfile(pickled_file):
           data = self.unpickle_data(pickled_file)
           
        data.update(some_dict)
        f = open(pickled_file, 'w')
        pickle.dump(data, f)
        f.close()
        
    @classmethod
    def unpickle_data(self, pickled_file):
        f  = open(pickled_file)
        data = pickle.load(f)
        f.close()
        return data
    
    
    @classmethod
    def exception_found(self,e, full_exc, now, file_name, name_of_tst, driver, *variables): #, driver_source):
            #print e
            error_timestamp= (now.strftime("%Y%m%d %H:%M"))
            #driver.get_screenshot_as_file('screenshot-%s.png' % now)
            test_data = (str(variables[0]))
            test_number =(str(variables[1]))
            captures_directory="Captures"
            if not os.path.exists(captures_directory):
                os.makedirs(captures_directory)
            driver.save_screenshot(captures_directory+"/%s_%s_%s.png"%(file_name, name_of_tst,test_number))
            driver_source = driver.page_source
            cur_url = str(driver.current_url)
            
            print("EXCEPTION Occurred in: %s "  % name_of_tst )
            #print str(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
            print(exc_type, "filename: " + str(fname), "Line number: " +str(exc_tb.tb_lineno))

            
            try:
                # This will create a new file or **overwrite an existing file**.
                f = open(captures_directory+"/errorsource_%s_%s_%s.html" % (file_name, name_of_tst,test_number), "w")
                try:
                    f.write('<html>')
                    f.write('<b>'+'Name of Test : ' + str(name_of_tst)+' '+'<br>') # Write a string to a file
                    f.write('Date and Time: ' +error_timestamp+' ' +'<br>')
                    f.write('Variables: ' + test_data + '<br>')
                    f.write('URL: '+cur_url +' '+ '</b>' + '<br>'+ '<br>')
                    f.write('<b>'+'(FOR QA ONLY) Specific Exception from Selenium:' +'</b>'+full_exc +'<br>' +'<br>')
                    f.writelines(driver_source) # Write a sequence of strings to a file
                    f.write('</html>')
                finally:
                    f.close()
            except IOError:
                pass

            return error_timestamp,full_exc, "filename: " + str(fname)

       
      
    @classmethod
    def find_element_by_sizzle(self,sizzle_selector, driver):   
        """
        Finds element by sizzle
    
        :Args:
        - sizzle locator: The sizzle selector to find the element
    
        :Return:
        - returns a WebElemnt 
        """
        time.sleep(3)
        sizzleLib = "(function(){function w(a,b,c,d,f,e){for(var f=0,g=d.length;f<g;f++){var h=d[f];if(h){for(var h=h[a],i=!1;h;){if(h.sizcache===c){i=d[h.sizset];break}if(h.nodeType===1&&!e)h.sizcache=c,h.sizset=f;if(h.nodeName.toLowerCase()===b){i=h;break}h=h[a]}d[f]=i}}}function x(a,b,c,d,f,e){for(var f=0,g=d.length;f<g;f++){var h=d[f];if(h){for(var h=h[a],i=!1;h;){if(h.sizcache===c){i=d[h.sizset];break}if(h.nodeType===1){if(!e)h.sizcache=c,h.sizset=f;if(typeof b!==\"string\"){if(h===b){i=!0;break}}else if(j.filter(b,[h]).length>0){i=h;break}}h=h[a]}d[f]=i}}}var u=/((?:\\((?:\\([^()]+\\)|[^()]+)+\\)|\\[(?:\\[[^\\[\\]]*\\]|['\"][^'\"]*['\"]|[^\\[\\]'\"]+)+\\]|\\\\.|[^ >+~,(\\[\\\\]+)+|[>+~])(\\s*,\\s*)?((?:.|\\r|\\n)*)/g,v=0,y=Object.prototype.toString,s=!1,z=!0;[0,0].sort(function(){z=!1;return 0});var j=function(a,b,c,d){var c=c||[],f=b=b||document;if(b.nodeType!==1&&b.nodeType!==9)return[];if(!a||typeof a!==\"string\")return c;var e=[],g,h,k,m,o=!0,r=j.isXML(b),p=a,l;do if(u.exec(\"\"),g=u.exec(p))if(p=g[3],e.push(g[1]),g[2]){m=g[3];break}while(g);if(e.length>1&&B.exec(a))if(e.length===2&&i.relative[e[0]])h=A(e[0]+e[1],b);else for(h=i.relative[e[0]]?[b]:j(e.shift(),b);e.length;)a=e.shift(),i.relative[a]&&(a+=e.shift()),h=A(a,h);else if(!d&&e.length>1&&b.nodeType===9&&!r&&i.match.ID.test(e[0])&&!i.match.ID.test(e[e.length-1])&&(g=j.find(e.shift(),b,r),b=g.expr?j.filter(g.expr,g.set)[0]:g.set[0]),b){g=d?{expr:e.pop(),set:n(d)}:j.find(e.pop(),e.length===1&&(e[0]===\"~\"||e[0]===\"+\")&&b.parentNode?b.parentNode:b,r);h=g.expr?j.filter(g.expr,g.set):g.set;for(e.length>0?k=n(h):o=!1;e.length;)g=l=e.pop(),i.relative[l]?g=e.pop():l=\"\",g==null&&(g=b),i.relative[l](k,g,r)}else k=[];k||(k=h);k||j.error(l||a);if(y.call(k)===\"[object Array]\")if(o)if(b&&b.nodeType===1)for(a=0;k[a]!=null;a++)k[a]&&(k[a]===!0||k[a].nodeType===1&&j.contains(b,k[a]))&&c.push(h[a]);else for(a=0;k[a]!=null;a++)k[a]&&k[a].nodeType===1&&c.push(h[a]);else c.push.apply(c,k);else n(k,c);m&&(j(m,f,c,d),j.uniqueSort(c));return c};j.uniqueSort=function(a){if(t&&(s=z,a.sort(t),s))for(var b=1;b<a.length;b++)a[b]===a[b-1]&&a.splice(b--,1);return a};j.matches=function(a,b){return j(a,null,null,b)};j.find=function(a,b,c){var d;if(!a)return[];for(var f=0,e=i.order.length;f<e;f++){var g=i.order[f],h;if(h=i.leftMatch[g].exec(a)){var j=h[1];h.splice(1,1);if(j.substr(j.length-1)!==\"\\\\\"&&(h[1]=(h[1]||\"\").replace(/\\\\/g,\"\"),d=i.find[g](h,b,c),d!=null)){a=a.replace(i.match[g],\"\");break}}}d||(d=b.getElementsByTagName(\"*\"));return{set:d,expr:a}};j.filter=function(a,b,c,d){for(var f=a,e=[],g=b,h,k,m=b&&b[0]&&j.isXML(b[0]);a&&b.length;){for(var o in i.filter)if((h=i.leftMatch[o].exec(a))!=null&&h[2]){var r=i.filter[o],p,l;l=h[1];k=!1;h.splice(1,1);if(l.substr(l.length-1)!==\"\\\\\"){g===e&&(e=[]);if(i.preFilter[o])if(h=i.preFilter[o](h,g,c,e,d,m)){if(h===!0)continue}else k=p=!0;if(h)for(var n=0;(l=g[n])!=null;n++)if(l){p=r(l,h,n,g);var q=d^!!p;c&&p!=null?q?k=!0:g[n]=!1:q&&(e.push(l),k=!0)}if(p!==void 0){c||(g=e);a=a.replace(i.match[o],\"\");if(!k)return[];break}}}if(a===f)if(k==null)j.error(a);else break;f=a}return g};j.error=function(a){throw\"Syntax error, unrecognized expression: \"+a;};var i=j.selectors={order:[\"ID\",\"NAME\",\"TAG\"],match:{ID:/#((?:[\\w\\u00c0-\\uFFFF\\-]|\\\\.)+)/,CLASS:/\\.((?:[\\w\\u00c0-\\uFFFF\\-]|\\\\.)+)/,NAME:/\\[name=['\"]*((?:[\\w\\u00c0-\\uFFFF\\-]|\\\\.)+)['\"]*\\]/,ATTR:/\\[\\s*((?:[\\w\\u00c0-\\uFFFF\\-]|\\\\.)+)\\s*(?:(\\S?=)\\s*(['\"]*)(.*?)\\3|)\\s*\\]/,TAG:/^((?:[\\w\\u00c0-\\uFFFF\\*\\-]|\\\\.)+)/,CHILD:/:(only|nth|last|first)-child(?:\\((even|odd|[\\dn+\\-]*)\\))?/,POS:/:(nth|eq|gt|lt|first|last|even|odd)(?:\\((\\d*)\\))?(?=[^\\-]|$)/,PSEUDO:/:((?:[\\w\\u00c0-\\uFFFF\\-]|\\\\.)+)(?:\\((['\"]?)((?:\\([^\\)]+\\)|[^\\(\\)]*)+)\\2\\))?/},leftMatch:{},attrMap:{\"class\":\"className\",\"for\":\"htmlFor\"},attrHandle:{href:function(a){return a.getAttribute(\"href\")}},relative:{\"+\":function(a,b){var c=typeof b===\"string\",d=c&&!/\\W/.test(b),c=c&&!d;d&&(b=b.toLowerCase());for(var d=0,f=a.length,e;d<f;d++)if(e=a[d]){for(;(e=e.previousSibling)&&e.nodeType!==1;);a[d]=c||e&&e.nodeName.toLowerCase()===b?e||!1:e===b}c&&j.filter(b,a,!0)},\">\":function(a,b){var c=typeof b===\"string\",d,f=0,e=a.length;if(c&&!/\\W/.test(b))for(b=b.toLowerCase();f<e;f++){if(d=a[f])c=d.parentNode,a[f]=c.nodeName.toLowerCase()===b?c:!1}else{for(;f<e;f++)(d=a[f])&&(a[f]=c?d.parentNode:d.parentNode===b);c&&j.filter(b,a,!0)}},\"\":function(a,b,c){var d=v++,f=x,e;typeof b===\"string\"&&!/\\W/.test(b)&&(e=b=b.toLowerCase(),f=w);f(\"parentNode\",b,d,a,e,c)},\"~\":function(a,b,c){var d=v++,f=x,e;typeof b===\"string\"&&!/\\W/.test(b)&&(e=b=b.toLowerCase(),f=w);f(\"previousSibling\",b,d,a,e,c)}},find:{ID:function(a,b,c){if(typeof b.getElementById!==\"undefined\"&&!c)return(a=b.getElementById(a[1]))&&a.parentNode?[a]:[]},NAME:function(a,b){if(typeof b.getElementsByName!==\"undefined\"){for(var c=[],d=b.getElementsByName(a[1]),f=0,e=d.length;f<e;f++)d[f].getAttribute(\"name\")===a[1]&&c.push(d[f]);return c.length===0?null:c}},TAG:function(a,b){return b.getElementsByTagName(a[1])}},preFilter:{CLASS:function(a,b,c,d,f,e){a=\" \"+a[1].replace(/\\\\/g,\"\")+\" \";if(e)return a;for(var e=0,g;(g=b[e])!=null;e++)g&&(f^(g.className&&(\" \"+g.className+\" \").replace(/[\\t\\n]/g,\" \").indexOf(a)>=0)?c||d.push(g):c&&(b[e]=!1));return!1},ID:function(a){return a[1].replace(/\\\\/g,\"\")},TAG:function(a){return a[1].toLowerCase()},CHILD:function(a){if(a[1]===\"nth\"){var b=/(-?)(\\d*)n((?:\\+|-)?\\d*)/.exec(a[2]===\"even\"&&\"2n\"||a[2]===\"odd\"&&\"2n+1\"||!/\\D/.test(a[2])&&\"0n+\"+a[2]||a[2]);a[2]=b[1]+(b[2]||1)-0;a[3]=b[3]-0}a[0]=v++;return a},ATTR:function(a,b,c,d,f,e){b=a[1].replace(/\\\\/g,\"\");!e&&i.attrMap[b]&&(a[1]=i.attrMap[b]);a[2]===\"~=\"&&(a[4]=\" \"+a[4]+\" \");return a},PSEUDO:function(a,b,c,d,f){if(a[1]===\"not\")if((u.exec(a[3])||\"\").length>1||/^\\w/.test(a[3]))a[3]=j(a[3],null,null,b);else return a=j.filter(a[3],b,c,1^f),c||d.push.apply(d,a),!1;else if(i.match.POS.test(a[0])||i.match.CHILD.test(a[0]))return!0;return a},POS:function(a){a.unshift(!0);return a}},filters:{enabled:function(a){return a.disabled===!1&&a.type!==\"hidden\"},disabled:function(a){return a.disabled===!0},checked:function(a){return a.checked===!0},selected:function(a){return a.selected===!0},parent:function(a){return!!a.firstChild},empty:function(a){return!a.firstChild},has:function(a,b,c){return!!j(c[3],a).length},header:function(a){return/h\\d/i.test(a.nodeName)},text:function(a){return\"text\"===a.type},radio:function(a){return\"radio\"===a.type},checkbox:function(a){return\"checkbox\"===a.type},file:function(a){return\"file\"===a.type},password:function(a){return\"password\"===a.type},submit:function(a){return\"submit\"===a.type},image:function(a){return\"image\"===a.type},reset:function(a){return\"reset\"===a.type},button:function(a){return\"button\"===a.type||a.nodeName.toLowerCase()===\"button\"},input:function(a){return/input|select|textarea|button/i.test(a.nodeName)}},setFilters:{first:function(a,b){return b===0},last:function(a,b,c,d){return b===d.length-1},even:function(a,b){return b%2===0},odd:function(a,b){return b%2===1},lt:function(a,b,c){return b<c[3]-0},gt:function(a,b,c){return b>c[3]-0},nth:function(a,b,c){return c[3]-0===b},eq:function(a,b,c){return c[3]-0===b}},filter:{PSEUDO:function(a,b,c,d){var f=b[1],e=i.filters[f];if(e)return e(a,c,b,d);else if(f===\"contains\")return(a.textContent||a.innerText||j.getText([a])||\"\").indexOf(b[3])>=0;else if(f===\"not\"){b=b[3];c=0;for(d=b.length;c<d;c++)if(b[c]===a)return!1;return!0}else j.error(\"Syntax error, unrecognized expression: \"+f)},CHILD:function(a,b){var c=b[1],d=a;switch(c){case \"only\":case \"first\":for(;d=d.previousSibling;)if(d.nodeType===1)return!1;if(c===\"first\")return!0;d=a;case \"last\":for(;d=d.nextSibling;)if(d.nodeType===1)return!1;return!0;case \"nth\":var c=b[2],f=b[3];if(c===1&&f===0)return!0;var e=b[0],g=a.parentNode;if(g&&(g.sizcache!==e||!a.nodeIndex)){for(var h=0,d=g.firstChild;d;d=d.nextSibling)if(d.nodeType===1)d.nodeIndex=++h;g.sizcache=e}d=a.nodeIndex-f;return c===0?d===0:d%c===0&&d/c>=0}},ID:function(a,b){return a.nodeType===1&&a.getAttribute(\"id\")===b},TAG:function(a,b){return b===\"*\"&&a.nodeType===1||a.nodeName.toLowerCase()===b},CLASS:function(a,b){return(\" \"+(a.className||a.getAttribute(\"class\"))+\" \").indexOf(b)>-1},ATTR:function(a,b){var c=b[1],c=i.attrHandle[c]?i.attrHandle[c](a):a[c]!=null?a[c]:a.getAttribute(c),d=c+\"\",f=b[2],e=b[4];return c==null?f===\"!=\":f===\"=\"?d===e:f===\"*=\"?d.indexOf(e)>=0:f===\"~=\"?(\" \"+d+\" \").indexOf(e)>=0:!e?d&&c!==!1:f===\"!=\"?d!==e:f===\"^=\"?d.indexOf(e)===0:f===\"$=\"?d.substr(d.length-e.length)===e:f===\"|=\"?d===e||d.substr(0,e.length+1)===e+\"-\":!1},POS:function(a,b,c,d){var f=i.setFilters[b[2]];if(f)return f(a,c,b,d)}}},B=i.match.POS,C=function(a,b){return\"\\\\\"+(b-0+1)},m;for(m in i.match)i.match[m]=RegExp(i.match[m].source+/(?![^\\[]*\\])(?![^\\(]*\\))/.source),i.leftMatch[m]=RegExp(/(^(?:.|\\r|\\n)*?)/.source+i.match[m].source.replace(/\\\\(\\d+)/g,C));var n=function(a,b){a=Array.prototype.slice.call(a,0);if(b)return b.push.apply(b,a),b;return a};try{Array.prototype.slice.call(document.documentElement.childNodes,0)}catch(D){n=function(a,b){var c=b||[],d=0;if(y.call(a)===\"[object Array]\")Array.prototype.push.apply(c,a);else if(typeof a.length===\"number\")for(var f=a.length;d<f;d++)c.push(a[d]);else for(;a[d];d++)c.push(a[d]);return c}}var t,q;document.documentElement.compareDocumentPosition?t=function(a,b){if(a===b)return s=!0,0;if(!a.compareDocumentPosition||!b.compareDocumentPosition)return a.compareDocumentPosition?-1:1;return a.compareDocumentPosition(b)&4?-1:1}:(t=function(a,b){var c=[],d=[],f=a.parentNode,e=b.parentNode,g=f;if(a===b)return s=!0,0;else if(f===e)return q(a,b);else if(f){if(!e)return 1}else return-1;for(;g;)c.unshift(g),g=g.parentNode;for(g=e;g;)d.unshift(g),g=g.parentNode;f=c.length;e=d.length;for(g=0;g<f&&g<e;g++)if(c[g]!==d[g])return q(c[g],d[g]);return g===f?q(a,d[g],-1):q(c[g],b,1)},q=function(a,b,c){if(a===b)return c;for(a=a.nextSibling;a;){if(a===b)return-1;a=a.nextSibling}return 1});j.getText=function(a){for(var b=\"\",c,d=0;a[d];d++)c=a[d],c.nodeType===3||c.nodeType===4?b+=c.nodeValue:c.nodeType!==8&&(b+=j.getText(c.childNodes));return b};(function(){var a=document.createElement(\"div\"),b=\"script\"+(new Date).getTime();a.innerHTML=\"<a name='\"+b+\"'/>\";var c=document.documentElement;c.insertBefore(a,c.firstChild);if(document.getElementById(b))i.find.ID=function(a,b,c){if(typeof b.getElementById!==\"undefined\"&&!c)return(b=b.getElementById(a[1]))?b.id===a[1]||typeof b.getAttributeNode!==\"undefined\"&&b.getAttributeNode(\"id\").nodeValue===a[1]?[b]:void 0:[]},i.filter.ID=function(a,b){var c=typeof a.getAttributeNode!==\"undefined\"&&a.getAttributeNode(\"id\");return a.nodeType===1&&c&&c.nodeValue===b};c.removeChild(a);c=a=null})();(function(){var a=document.createElement(\"div\");a.appendChild(document.createComment(\"\"));if(a.getElementsByTagName(\"*\").length>0)i.find.TAG=function(a,c){var d=c.getElementsByTagName(a[1]);if(a[1]===\"*\"){for(var f=[],e=0;d[e];e++)d[e].nodeType===1&&f.push(d[e]);d=f}return d};a.innerHTML=\"<a href='#'></a>\";if(a.firstChild&&typeof a.firstChild.getAttribute!==\"undefined\"&&a.firstChild.getAttribute(\"href\")!==\"#\")i.attrHandle.href=function(a){return a.getAttribute(\"href\",2)};a=null})();document.querySelectorAll&&function(){var a=j,b=document.createElement(\"div\");b.innerHTML=\"<p class='TEST'></p>\";if(!(b.querySelectorAll&&b.querySelectorAll(\".TEST\").length===0)){j=function(b,c,e,g){c=c||document;if(!g&&c.nodeType===9&&!j.isXML(c))try{return n(c.querySelectorAll(b),e)}catch(h){}return a(b,c,e,g)};for(var c in a)j[c]=a[c];b=null}}();(function(){var a=document.createElement(\"div\");a.innerHTML=\"<div class='test e'></div><div class='test'></div>\";if(a.getElementsByClassName&&a.getElementsByClassName(\"e\").length!==0&&(a.lastChild.className=\"e\",a.getElementsByClassName(\"e\").length!==1))i.order.splice(1,0,\"CLASS\"),i.find.CLASS=function(a,c,d){if(typeof c.getElementsByClassName!==\"undefined\"&&!d)return c.getElementsByClassName(a[1])},a=null})();j.contains=document.compareDocumentPosition?function(a,b){return!!(a.compareDocumentPosition(b)&16)}:function(a,b){return a!==b&&(a.contains?a.contains(b):!0)};j.isXML=function(a){return(a=(a?a.ownerDocument||a:0).documentElement)?a.nodeName!==\"HTML\":!1};var A=function(a,b){for(var c=[],d=\"\",f,e=b.nodeType?[b]:b;f=i.match.PSEUDO.exec(a);)d+=f[0],a=a.replace(i.match.PSEUDO,\"\");a=i.relative[a]?a+\"*\":a;f=0;for(var g=e.length;f<g;f++)j(a,e[f],c);return j.filter(d,c)};window.Sizzle=j})();"
        driver.execute_script(sizzleLib)
        elem = driver.execute_script("return Sizzle(arguments[0])", sizzle_selector)
        
        print "Seeking this selector: ",sizzle_selector
        return elem[0] if elem else 'Unable to find: %s' % (sizzle_selector)
        ##needs try except and to return the exception content if issue
        
    @classmethod
    def get_csv_data(self,file_name):
        original = file(file_name, 'rU')
        reader = csv.reader(original)
        data_list=[]
        
        
        for row in reader:
            #will print each row by itself (all columns from names up to what they wear)
            #print row
            
            data_list.append(row)
            
        return data_list


    @classmethod
    def get_popup_windows(self, window_handles, parent_window):
        
        #print "Window handles",window_handles, "parent window", parent_window
        popup_windows = []
        for window in window_handles:
            if window != parent_window:
                #print ("Adding to popup window list: "+ window)
                popup_windows.append(window)
        
        #print popup_windows
        
        return popup_windows        

    @classmethod
    def switch_to_window_by_title(self, driver, title):
        
        window_handles = driver.window_handles
        print "cur windows",window_handles
        #print "Window handles",window_handles, "parent window", parent_window
        for window in window_handles:
            print window.title()
            
            if window != parent_window:
                #print ("Adding to popup window list: "+ window)
                popup_windows.append(window)
        
        #print popup_windows
        
        return popup_windows
 

class SeleniumSQLHelper():
    
    
    option = env_variable
    config = SeleniumTestHelperTwo.environment_setter(option)
    print config.our_db
    connect_string = "DRIVER={SQL Server};SERVER=lithium.wsg.com;DATABASE=%s;" % (config.our_db) + "Trusted_Connection=yes"

    @classmethod
    def sql_data_fetch(self, sql, *inp_params):
        time.sleep(3)
        #print "sql data fetch inp_params",inp_params
        cnxn = pyodbc.connect(SeleniumSQLHelper.connect_string)
        cursor = cnxn.cursor()
        print "(sql, inp_params): ", (sql, inp_params)
        cursor.execute(sql, inp_params)
        rows = cursor.fetchall()
        
        result= []
        for row in rows:
            #print row
            result.append(row)
        #print paxs
         
        cursor.close()
        cnxn.close()
        
        try:
            result[0][:]
        except IndexError:
            result="0_DB_Results. "
            print result 
            return result
        
        print "DB Results: ",tuple(result)
        return tuple(result)



    @classmethod
    def sql_data_modify(self,sql, *inp_params):
        cnxn = pyodbc.connect(SeleniumSQLHelper.connect_string)
        cursor = cnxn.cursor()
        
        cursor.execute(sql, inp_params)
        cnxn.commit()
        #print "Number of rows affected by rejecting checkin: %s" % str(cursor.rowcount)
        
        cursor.close()
        cnxn.close()




        

class IWTtestHelperTwo(unittest.TestCase):
    def __init__(self):
        pass
        
    def typical_test_case(self,name_of_tst, *kwargs):
        now = datetime.datetime.now()
        time_list= (" time is:  ", now.strftime("%Y-%m-%d %H:%M:%S"))
        print time_list
        #name_of_tst=(str(inspect.stack()[0][3]))
        print "name of test(we don't want it to be: typical_test_case )", name_of_tst
        #self.assertEqual(1, "typical testcase failure")
        return name_of_tst, now
        
    def intrax_login(self, driver,INTRAX, INTRAX_login):
    
        driver.get(base_url  + INTRAX + "/ext/login.action")
        driver.find_element_by_css_selector("#j_username").clear()
        driver.find_element_by_css_selector("#j_username").send_keys(INTRAX_login)
        driver.find_element_by_id("j_password").clear()
        driver.find_element_by_id("j_password").send_keys("changeme")
        driver.find_element_by_name("login").click()
#        try: self.assertEqual("Samuel Safyan", driver.find_element_by_css_selector("strong").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))

    
    def pxr_login(self, driver,PXR, PXR_custom_login):
    
        driver.get(base_url  + PXR + "/ext/login.action")
        driver.find_element_by_css_selector("#j_username").clear()
        driver.find_element_by_css_selector("#j_username").send_keys(PXR_custom_login)
        driver.find_element_by_id("j_password").clear()
        driver.find_element_by_id("j_password").send_keys("changeme")
        driver.find_element_by_name("login").click()
        
    def csv_address_start_end(self,rand_avw_addr, csv_file):
        tst_user_list = SeleniumTestHelperTwo.get_csv_data(csv_file)
        
        if rand_avw_addr=="random":
            print "selecting a RANDOM address from address file"
            start_num=random.randrange(1,len(tst_user_list))
            end_num=start_num+1
            return tst_user_list[start_num:end_num] 
        elif rand_avw_addr=="fixed":
            print "selecting a FIXED address from address file"
            #start_num=9
            #end_num=10
            return [tst_user_list[9],] 
        else:
            """Should loop through all """
            return tst_user_list[1:]
            print "Data driven testing through address list in desc order"
            #start_num=1
            #end_num=len(tst_user_list)
            #return start_num, end_num 
    
    def avw_address_result(self, csv_data,*kwargs):
        """This test queries the DB and to see that the address table got updated with CSV data.
        Disabled the wehnmodfied due to clock issues on stage and no one fixing them"""
        #self.assertEqual(1,"hi")
        #address_result = ["addy 1", "addy2", "city"]
        address_result = SeleniumSQLHelper.sql_data_fetch("""
                select top 1 Street1, Street2, City, StateDtl.Abbr, PostalCode,
                  -- CAST(GeocodeId AS varchar(20)) as GeocodeID
                 convert(varchar(15), isnull(Longitude, 0)), convert(varchar(15), isnull(Latitude, 0)), convert(varchar(15), isnull(GeocodeID,0))
                 from address
                join StateDtl
                on Address.StateID= StateDtl.StateID
                --and PartyID= ?
                --and WhenModified >=  DATEADD(minute, -2, GETDATE())  
                --and addressid =1392650
                order by AddressID desc
                
                            """)                                                
        
        time.sleep(3)               
        
        print "Address_result_from db: ", address_result[0][:], "address from CSV: ", tuple(csv_data)
        
        #self.assertEqual(1,"hi")
        self.assertTupleEqual(tuple(address_result[0][:]), tuple(csv_data))                                      

    @classmethod
    def pxr_job_change_fill_in(self,driver,pax_jc_id,pxr_job_change_start_date,pxr_job_change_end_date):
    
        
        company_name ="TD Sam%s" % pax_jc_id
        supervisor_name ="TestSuper%s" % pax_jc_id
        driver.find_element_by_css_selector("input.termsConditions").click()
        driver.find_element_by_xpath("(//input[@type='checkbox'])[2]").click()
        
        driver.find_element_by_css_selector("input#hostCompanyName").clear()
        driver.find_element_by_id("icdRipa.supervisor").clear()
        driver.find_element_by_css_selector("input#hostCompanyName").send_keys(company_name)
        driver.find_element_by_id("icdRipa.supervisor").send_keys(supervisor_name)
        driver.find_element_by_id("icdRipa.supervisorEmail").clear()
        driver.find_element_by_id("icdRipa.supervisorEmail").send_keys("superemail@lll.com")
        
        driver.find_element_by_css_selector("#hostCompanyPhoneAreaCode").clear()
        driver.find_element_by_css_selector("#hostCompanyPhoneAreaCode").send_keys("415")
        driver.find_element_by_css_selector("#hostCompanyPhoneNumberPrefix").clear()
        driver.find_element_by_css_selector("#hostCompanyPhoneNumberPrefix").send_keys("555")
        driver.find_element_by_css_selector("#hostCompanyPhoneNumberSuffix").clear()
        driver.find_element_by_css_selector("#hostCompanyPhoneNumberSuffix").send_keys("5555")
        driver.find_element_by_css_selector("#icdJobChangeForm_icdRipa_startDate").clear()
        
        ##need code/ select calendar.
        driver.find_element_by_css_selector("#icdJobChangeForm_icdRipa_startDate").clear()
        driver.find_element_by_css_selector("#icdJobChangeForm_icdRipa_startDate").send_keys(pxr_job_change_start_date)
        driver.find_element_by_css_selector("#icdJobChangeForm_icdRipa_endDate").clear()
        driver.find_element_by_css_selector("#icdJobChangeForm_icdRipa_endDate").send_keys(pxr_job_change_end_date)
        driver.find_element_by_id("icdRipa.jobTitle").clear()
        driver.find_element_by_id("icdRipa.jobTitle").send_keys("Supervisor")
        driver.find_element_by_id("icdRipa.estimatedPayRate").clear()
        driver.find_element_by_id("icdRipa.estimatedPayRate").send_keys("55/hr")
                
        driver.find_element_by_id("icdRipa.jobDescription").clear()
        driver.find_element_by_id("icdRipa.jobDescription").send_keys("JD description")
        driver.find_element_by_css_selector("#participantPhoneAreaCode").clear()
        driver.find_element_by_css_selector("#participantPhoneAreaCode").send_keys("111")
        driver.find_element_by_css_selector("#participantPhoneNumberPrefix").clear()
        driver.find_element_by_css_selector("#participantPhoneNumberPrefix").send_keys("111")
        driver.find_element_by_css_selector("#participantPhoneNumberSuffix").clear()
        driver.find_element_by_css_selector("#participantPhoneNumberSuffix").send_keys("1111")
        print 
        return company_name           
          
    
    def pluto_job_remove(self,driver, INTRAX,INTRAX_login, pax_jc_id):
        sleep_time = 7
        self.intrax_login(driver, INTRAX, INTRAX_login)
        
        driver.get(base_url + INTRAX + "/icd/issue/viewICDIssue.action?icdParticipantId=%s" % pax_jc_id)
        Select(driver.find_element_by_css_selector("#icdIssueForm_icdIssue_issueType")).select_by_visible_text("Complaint: Hours - Excessive")
        SeleniumTestHelperTwo.find_element_by_sizzle("td:contains('Remove from current') input", driver).click()
        
        tst_user_list = SeleniumTestHelperTwo.get_csv_data("iwt_users.csv") 
        
        driver.find_element_by_css_selector("#iceAddress_1_street_1").clear()
        driver.find_element_by_css_selector("#iceAddress_1_street_1").send_keys("1350 10th Ave")
        driver.find_element_by_css_selector("#iceAddress_1_street_2").clear()
        driver.find_element_by_css_selector("#iceAddress_1_city").clear()
        driver.find_element_by_css_selector("#iceAddress_1_city").send_keys("San Francisco")
        driver.find_element_by_css_selector("#iceAddress_1_postalCode").clear()
        driver.find_element_by_css_selector("#iceAddress_1_postalCode").send_keys("94122")
        time.sleep(1)
        Select(driver.find_element_by_css_selector("#iceAddress_1_state")).select_by_visible_text("California")
        time.sleep(2)
        driver.find_element_by_css_selector("input.saveButtonImage").click()
        time.sleep(3)
        
        
        try:
            avw_success_element = '#successMessages'
            driver.find_element_by_css_selector(avw_success_element)

        except Exception as e:
                print e
                time.sleep(3)
                avw_console=driver.find_element_by_css_selector("div#AVWConsole").text
                print "AVW message was: "+ avw_console
                
                if avw_console ==('We found an address that closely matches what you entered. Once you are sure that the information below is correct, please click "Use This Address".'):
                            print ("Accepting suggested address")
                            driver.find_element_by_css_selector("button#AVWAcceptButton-button").click()
                            time.sleep(sleep_time)
        
        return "Finished removing Pax. Returning tst_user_list ",tst_user_list

    def monthly_contact(self, driver,*kwargs):
        dateStamp=kwargs[0]
        name_of_tst = kwargs[1]
        
        print ("Starting monthly contact")
        driver.find_element_by_css_selector("div.sg-question-title")
        
        driver.find_element_by_css_selector("#sgE-923012-1-3-10002").click()
        driver.find_element_by_css_selector("#sgE-923012-1-4-element").clear()
        driver.find_element_by_css_selector("#sgE-923012-1-4-element").send_keys(dateStamp)
        driver.find_element_by_css_selector("#sgE-923012-1-5-10003").click()
    
        driver.find_element_by_css_selector("#sgE-923012-1-7-10007").click()
        
        # Q4. Monthly Activities 
        driver.find_element_by_css_selector("#sgE-923012-1-9-10029").click()
        # Q5. Rate your experience
        driver.find_element_by_css_selector("#sgE-923012-1-10-10012").click()
        driver.find_element_by_css_selector("#sg_SubmitButton").click()
        print ("Finished monthly contact")
        time.sleep(3)
    


    def address_fill_in(self,driver, row):
        now = datetime.datetime.now()
        print("typing info for: "+str(row), " time is:  ", now.strftime("%Y-%m-%d %H:%M:%S"))
        driver.find_element_by_css_selector("input#iceAddress_1_street_1").clear()
        driver.find_element_by_css_selector("input#iceAddress_1_street_1").send_keys(row[1])
        #time.sleep(2)
        driver.find_element_by_css_selector("input#iceAddress_1_street_2").clear()
        driver.find_element_by_css_selector("input#iceAddress_1_street_2").send_keys(row[2])
        #time.sleep(2)
        driver.find_element_by_css_selector("input#iceAddress_1_city").clear()
        driver.find_element_by_css_selector("input#iceAddress_1_city").send_keys(row[3])
        time.sleep(1)
        driver.find_element_by_css_selector("input#iceAddress_1_postalCode").clear()
        driver.find_element_by_css_selector("input#iceAddress_1_postalCode").send_keys(row[5])
        time.sleep(2)
        Select(driver.find_element_by_css_selector("select#iceAddress_1_state")).select_by_visible_text(row[4])
        time.sleep(3)
    
    def avw_test(self,driver,name_of_tst, row, override, submit, avw_success_element,success_text):
#        try:
            self.address_fill_in(driver, row)
            sleep_time=7
            print("Submitting data")
            
            driver.find_element_by_css_selector(submit).click()
            print "Submitted data"
            time.sleep(sleep_time)
            
            try:
                evaled_element= eval(avw_success_element)
                print "Evaled element!!", evaled_element
#                self.assertEqual(evaled_element , success_text) 
                self.assertRegexpMatches(evaled_element,success_text)
                print "Success. Skipping AVW tests, since" +  evaled_element + " matches " +  success_text
    
            except Exception as e:
                print ("Avw has been invoked, as this success_text was not found: "+success_text)
                print e
                time.sleep(3)
                avw_console=driver.find_element_by_css_selector("div#AVWConsole").text
                print "AVW message was: "+ avw_console
                
                if row[0]=="valid_no_suite":
                   
                    print ("Attempting to submit without suite")
                    #if self.is_element_present(driver, By.CSS_SELECTOR, "zzzzbutton#AVWOverrideButton-button") == 1:
        
                    for i in range(override):
                        driver.find_element_by_css_selector("button#AVWAcceptButton-button").click()
                        time.sleep(sleep_time) 
                    driver.find_element_by_css_selector("button#AVWOverrideButton-button").click()
                    time.sleep(sleep_time)
                    
    
     
                
                elif row[0]=="valid_med_override_grant":
                     
                    
                    for i in range(override):
                        
                        driver.find_element_by_css_selector("input#postalCode.avwField").clear()
                        time.sleep(1)
                        driver.find_element_by_css_selector("input#postalCode.avwField").send_keys(row[5])
                        time.sleep(2)
                        #self.address_fill_in(driver, tst_user_list,row)
                        driver.find_element_by_css_selector("button#AVWAcceptButton-button").click()
                        time.sleep(sleep_time) 
                    driver.find_element_by_css_selector("button#AVWOverrideButton-button").click()
                    time.sleep(sleep_time)
                    
                
                
                elif row[0]=="override_medium_slt":
                    print ("Attempting to submit without abbreviated city")
                    
                    for i in range(override):
                        
                        time.sleep(2)
                        driver.find_element_by_css_selector("input#city.avwField").clear()
                        driver.find_element_by_css_selector("input#city.avwField").send_keys(row[3])
                        time.sleep(2)
                        driver.find_element_by_css_selector("input#street1.avwField").clear()
                        driver.find_element_by_css_selector("input#street1.avwField").send_keys(row[1])
                        driver.find_element_by_css_selector("input#postalCode.avwField").clear()
                        driver.find_element_by_css_selector("input#postalCode.avwField").send_keys(row[5])
                        time.sleep(2)
                        driver.find_element_by_css_selector("button#AVWAcceptButton-button").click()
                        time.sleep(sleep_time) 
                    driver.find_element_by_css_selector("button#AVWOverrideButton-button").click()
                    time.sleep(sleep_time)
                    
    
                elif avw_console ==('We found an address that closely matches what you entered. Once you are sure that the information below is correct, please click "Use This Address".'):
                    print ("Accepting suggested address")
                    driver.find_element_by_css_selector("button#AVWAcceptButton-button").click()
                    time.sleep(sleep_time)
                
                elif avw_console==('We were unable to verify the address that you entered. Please double-check the information you entered and resubmit.'):
                    
                    try:
                        driver.find_element_by_css_selector("button#AVWOverrideButton-button").click()
                        print "clicked button#AVWOverrideButton-button" 
                    except:
                        for i in range(override):
                            driver.find_element_by_css_selector("button#AVWAcceptButton-button").click()
                            time.sleep(sleep_time)
    #                        for j in range(11):
    #                             try:
    #                                if driver.is_element_present(By.CSS_SELECTOR, "div#AVWOverlayHeader"):
    #                                    print "Overlay still here"
    #                             except: pass
    #                             time.sleep(1)
    #                        else: self.fail("time out waiting for button")
                            
                        driver.find_element_by_css_selector("button#AVWOverrideButton-button").click()
                           
                            
                    
                    
                elif avw_console==('In most cases, a P.O. Box is not an acceptable physical address. If you are certain that this information is correct, please click "Resubmit".'):
                    print ("Po Box Avw test")
                    ## PROBLEM IS HERE for PXR vs pluto situation
                    override=1
                    if override >0:
                        for i in range(override):
    #                        print ("override",override)
    #                        print ("i",i)
                            driver.find_element_by_css_selector("input#street1.avwField").clear()
                            driver.find_element_by_css_selector("input#street1.avwField").send_keys(tst_user_list[row][1])
                            driver.find_element_by_css_selector("input#postalCode.avwField").clear()
                            driver.find_element_by_css_selector("input#postalCode.avwField").send_keys(tst_user_list[row][5])
                            time.sleep(2)
                            driver.find_element_by_css_selector("button#AVWAcceptButton-button").click()
                            time.sleep(sleep_time) 
                    else:  
                        driver.find_element_by_css_selector("button#AVWOverrideButton-button").click()
                        time.sleep(sleep_time)
                    
                elif avw_console==('The address you submitted is a Commercial Delivery Point and is not an acceptable physical address. If you are certain that this information is correct, please click "Resubmit".'):
                    print ("U-Commerical Delivery Avw test")
                    driver.find_element_by_css_selector("button#AVWAcceptButton-button").click()
                    time.sleep(3)
                    
                    for i in range(override):
                        ("PO box override #",i)
                        driver.find_element_by_css_selector("button#AVWAcceptButton-button").click()
                        time.sleep(sleep_time)       
                        
                    driver.find_element_by_css_selector("button#AVWOverrideButton-button").click()
                    time.sleep(sleep_time)
                
                elif avw_console==('We found multiple addresses that closely match what you entered. Please select the correct address below. If none of these are correct, please click "Cancel" to try again.'):
                    print("Multiples Test")
                    time.sleep(2)
                    driver.find_element_by_css_selector("button#AVWAcceptButton-button").click()
                    
                    print("running multiple floors scenario")
                    time.sleep(2)
                    avw_console=driver.find_element_by_css_selector("#AVWConsole").text
                    if avw_console==('The address you entered appears to be missing either a floor, apartment or suite number. Please double-check the information you entered and resubmit.'):
                        print ("Typing in floors")
                        time.sleep(2)
                        driver.find_element_by_css_selector("input[name=\"street2\"]").clear()
                        driver.find_element_by_css_selector("input[name=\"street2\"]").send_keys("Fl 11")
                        driver.find_element_by_css_selector("input#street1.avwField").send_keys("")
                        time.sleep(2)
                        driver.find_element_by_css_selector("button#AVWAcceptButton-button").click()
                        time.sleep(sleep_time)
                                
                        ## will fail due to unbound method assertRegexpMatches() must be called with IWTtestHelper instance as first argument (got unicode instance instead)
    #                    try:                         
    #                        unittest.TestCase.assertRegexpMatches(driver.find_element_by_css_selector("div#successMessages").text, r"^[\s\S]*The address has been saved successfully[\s\S]*$")
    #                        print ("Multiple Floors scenario success")
    #                    except Exception as e: 
    #                        print ("ERROR: Multiple floors scenario failed due to %s" % e)
                    
                        
                elif avw_console==('The address you entered appears to be missing either a floor, apartment or suite number. Please double-check the information you entered and resubmit.'):
                        print ("Typing in floors")
                        time.sleep(2)
                        driver.find_element_by_css_selector("input[name=\"street2\"]").clear()
                        driver.find_element_by_css_selector("input[name=\"street2\"]").send_keys("Fl 11")
                        time.sleep(2)
                        
                                
                        for i in range(override):
                            ("override #",i)
                            driver.find_element_by_css_selector("button#AVWAcceptButton-button").click()
                            time.sleep(sleep_time)       
                            
                        driver.find_element_by_css_selector("button#AVWAcceptButton-button").click()
                        time.sleep(sleep_time)
                
                #self.assertEqual(evaled_element , success_text)                                              
                
                 
                print "AVW is finished, potentially succesfully"
            
#        except Exception as e:
#            print "Exception: "+ str(e)
#            self.fail(e)



class AyusaTestHelper(unittest.TestCase):
    def __init__(self):
        pass
    
    def nemo_login(self, driver, NEMO, NEMO_login):
        driver.get(base_url + NEMO + "/index.cfm")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(NEMO_login)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("changeme")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        
       
    def party_lookup(self, driver, element_locator, party_input_locator):
        
            #SeleniumTestHelper.SeleniumTestHelperTwo.find_element_by_sizzle(lookup_locator, driver).click()
            eval(element_locator)
            time.sleep(5)
            driver.switch_to_window(driver.window_handles[-1])
            driver.switch_to_frame(0)
            driver.find_element_by_name("searchtxt").clear()
            driver.find_element_by_name("searchtxt").send_keys("a")
            
            driver.find_element_by_name("btnsearch").click()
            driver.switch_to_window(driver.window_handles[-1])
            driver.switch_to_frame(1)
            driver.find_element_by_name(party_input_locator).click()
            
            driver.switch_to_window(driver.window_handles[-1])
            driver.switch_to_frame(2)
            driver.find_element_by_name("OKbtn").click()
            time.sleep(4)
    
if __name__ == '__main__':    
    unittest.main()







