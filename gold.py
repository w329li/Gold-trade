#!/usr/bin/python
# encoding:utf-8
import urllib, json, urllib2, requests
import time
import datetime as dt


#####define customer class first



####define the customer class
class Customer:
    '''Fields: userID(Str),password(Str),gold(float),deposit(float)'''
    def __init__(self,id,password,gold,money):
                self.userID = id
                self.password = password
                self.gold = gold
                self.deposit = money

                print("now create a customer")
                name = input("please input userID")
                while (true):
                    password = input("please input password")
                    recheck = input("please re-input password")
                    if (password == recheck): break
                    else: print("password is wrong!")


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



