#!/usr/bin/python
# encoding:utf-8
import urllib, json, urllib2, requests
import time
import datetime as dt


#####define customer class first



####define the customer class
class Customer:
    '''Fields: userID(Str),password(Str),gold(float),deposit(float),
        upper(float),lower(float),trade(float),build_trade(bool)'''
    def __init__(self,id,password,gold,money):
                self.userID = id
                self.password = password
                self.gold = gold
                self.deposit = money
                self.trade = 0
                self.build_trade= False
                self.message()
                print("new Customer initialized")
                print("do you want to build a automatic trade right now?(y/n)")
                answer = raw_input()
                if (answer == "y"):
                    self.build_trade = True
                    self.upper = float(input("set up upper bound: "))
                    self.lower = float(input("set up lower bound: "))
                    self.trade = float(input("set the trade amount of gold: "))
                self.message()
                print("\n")



    def message(self):
        print("userID: "+ str(self.userID))
        print("current gold deposit: "+ str(self.gold))
        print("current money deposit: "+ str(self.deposit))
        auto_trade  = self.build_trade
        if (auto_trade): print("automatic trade already build up")
        else: print("automatic trade have not build up")



    def check_price(self,price):
        if (self.build_trade == True):
            if (price >= self.upper):
                sell = self.trade * price ## calculate the price of gold u want to sell
                self.deposit += sell
                self.gold -= self.trade
            elif (price <= self.lower):
                buy = self.trade * price ## calculate price of gold u want to buy
                cost = self.deposit - buy
                if (cost <= 0): ## client's deposit is not enough to buy so many gold
                    buy = self.deposit / price
                    self.gold += buy
                    self.deposit = 0
                else:
                    self.gold += self.trade
                    self.deposit -= buy
                    self.trade = 0 ## reset the trade amount
            ### otherwise we do not do any operation
            self.build_trade = False
            self.message()
            print("\n")
            return
        elif (self.build_trade== False):
            self.message()
            print("\n")
            return




print("now create a customer")
name = raw_input("please input userID: ")
password = raw_input("please input password: ")

while (True):
    recheck = raw_input("please re-input password: ")
    if (password == recheck): break
    else: print("password is wrong!")

gold = float(input("please input gold amount: "))
deposit = float(input("please input initial deposit: "))


client = Customer(name,password,gold,deposit)





###############################################################
## now we build the API connection to get current gold price
###############################################################


data = {}
data["appkey"] = "apppkey"

url_value = urllib.urlencode(data)
url = "requested_url" + url_value
#request = urllib2.Request(url)
#result = urllib2.urlopen(request)
#jsonarr = result.json()
result = requests.get(url).json()
i = 0
while(i < 5):
    time.sleep(5)
    current_price = float(result["result"][0]["price"])
    temp_peak = float(result["result"][0]["maxprice"])
    temp_trough = float(result["result"][0]["minprice"])
    ##change_percent = (result["result"][0]["changepercent"])
    ##last_closing_price = result["result"][0]["lastclosingprice"]
    time = result["result"][0]["updatetime"]
    print("Current gold price: "+ str(current_price))
    print("Contemporary peak: "+ str(temp_peak))
    print("Contemporary trough: "+ str(temp_trough))
    ##print("Change percent: "+ str(change_percent))
    ##print("Last closing price: "+ str(last_closing_price))
    print("Current time: "+ str(time))
    client.check_price(current_price)
    i += 1



