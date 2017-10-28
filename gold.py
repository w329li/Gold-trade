#!/usr/bin/python
# encoding:utf-8
import urllib, json, urllib2, requests
import time
import datetime as dt

data = {}
data["appkey"] = "8a815caa8cc5e08c"

url_value = urllib.urlencode(data)
url = "http://api.jisuapi.com/gold/shgold"+"?"+url_value
#request = urllib2.Request(url)
#result = urllib2.urlopen(request)
#jsonarr = result.json()
result = requests.get(url).json()
i = 0
while(i < 5):
  time.sleep(5)
  print(result["result"][0]["price"])
  i += 1
