
#!/usr/bin/python

import os
import json
import cgi

acc = os.environ.get("HTTP_ACCEPT", "No accept header")



qur = os.environ.get("QUERY_STRING", "No Query String in url")


if str(qur) == "foo":
        url = "http://google.com/"
        print "Status: 302 Moved"
        print "Location: %s" % url
        print
elif str(qur) == "amazon":
        url = "http://amazon.com/"
        print "Status: 302 Moved"
        print "Location: %s" % url
        print
elif str(qur) == "walmart":
        url = "http://walmart.com/"
        print "Status: 302 Moved"
        print "Location: %s" % url
        print
else:
     	print "<html><body>"
        for headername, headervalue in os.environ.iteritems():
            if headername.startswith("HTTP_"):
                print "<p>{0} = {1}</p>".format(headername, headervalue)

        print "</html></body>"

        print os.environ.get("QUERY_STRING", "No Query String in url")

        import sys
        data = sys.stdin.read()
        print data

        if str(acc) == "application/vnd.byu.cs462.v1+json":
                print "Content-Type: application/json"
                response = {"version": "v1" }
                print
                print json.JSONEncoder().encode(response)


        if str(acc) == "application/vnd.byu.cs462.v2+json":
                print "Content-Type: application/json"
                response = {"version": "v2" }
                print
                print json.JSONEncoder().encode(response) 


        print




