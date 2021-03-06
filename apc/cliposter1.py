import httplib
import base64
import string
 
url = "/"
username = 'apc'
password = 'apc'
message = 'some message'

data = open("hostlist.txt")
for host in data:
    host = host.strip('\r\n')
    # base64 encode the username and password
    auth = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    try:
        webservice = httplib.HTTP(host)
        # write your headers
        webservice.putrequest("POST", url)
        webservice.putheader("Host", host)
        webservice.putheader("User-Agent", "Python http auth")
        webservice.putheader("Content-type", "text/html; charset=\"UTF-8\"")
        webservice.putheader("Content-length", "%d" % len(message))
        # write the Authorization header like: 'Basic base64encode(username + ':' + password)
        webservice.putheader("Authorization", "Basic %s" % auth)
        webservice.endheaders()
        webservice.send(message)
        # get the response
        statuscode, statusmessage, header = webservice.getreply()
        print "Checking APC unit,", host,',',statuscode,',',statusmessage
        #print "Response: ", host, statuscode, statusmessage
        #print "Headers: ", header
        res = webservice.getfile().read()
        #print 'Content: ', res
    except:
        print "APC unit,", host, ", timeout"
