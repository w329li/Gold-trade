#!/usr/bin/python
# encoding:utf-8
import urllib, json, urllib2, requests
import time
import datetime as dt

data = {}
data["appkey"] = "8a815caa8cc5e08c"

url_value = urllib.urlencode(data)
url = "http://api.jisuapi.com/gold/shgold"+"?"+url_value
request = urllib2.Request(url)
result = urllib2.urlopen(request)
jsonarr = json.loads(result.read())
print(jsonarr)

start_time = dt.datetime.today().timestamp()
i = 0
while(i < 5):
  time.sleep(5)
  print(i)
  i += 1


