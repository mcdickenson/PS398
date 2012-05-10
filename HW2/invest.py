""" Homework 2
Computational Frameworks, POLS 398
Spring 2012, Duke University
Matt Dickenson """
# try using Exceptions

import random
import ystockquote

class Portfolio(object):

     def __init__(self):
        self.transactions = ""
        self.cashBalance = 0 
        self.stockBalance = {} # this will be a dict of dicts
        self.mfBalance = {}

     def __str__(self):
        self.stock_list = ""
        for i in range(len(self.stockBalance)):
            new_string = str(self.stockBalance[i]["shares"]) + ' ' + str(self.stockBalance[i]["symbol"])
            if len(self.stockBalance) > i : # may need to be i + 1 
                new_string += '\n'
            self.stock_list += new_string

        self.mf_list = ""
        for i in range(len(self.mfBalance)):
            new_string = str(self.mfBalance[i]["shares"]) + ' ' + str(self.mfBalance[i]["symbol"])
            if len(self.mfBalance) > i : 
                new_string += '\n'
            self.mf_list += new_string
        
        return "cash: $%s \nstock: %s \nmutual funds: %s" % (self.cashBalance, self.stock_list, self.mf_list)

     def history(self):
        print self.transactions
     
     def addCash(self, amount):
        self.cashBalance += amount
        self.transactions += ("$%.2f added.\n" % amount)

     def withdrawCash(self, amount):
        self.cashBalance -= amount # don't withdraw negative money
                                   # check the amt to be withdrawn
        self.transactions += ("$%.2f withdrawn. \n" % amount)

     def buyStock(self, shares, stock): # what if i'm buying for the 2
        purchase_amount = shares * stock.price
        if (shares % 1 == 0) & (purchase_amount <= self.cashBalance):
            self.cashBalance -= purchase_amount
           self.stockBalance[len(self.stockBalance)] = {"symbol": stock.name, "shares": shares, "object": stock} # the way this is being used it might as well be a list
                                                                                                                 # what is returned if this works?
              
            self.transactions += ("Purchased %s shares of %s stock at $%.2f per share, for a total of $%.2f.\n" % (shares, stock.name, stock.price, purchase_amount))

        elif (shares % 1 == 0) & (purchase_amount > self.cashBalance):
            return "That purchase exceeds your cash balance of %.2f. Please enter a smaller purchase." % self.cashBalance

        elif (shares % 1 != 0):
            return "Fractional shares cannot be purchased. Please enter a whole number of shares."

        else: return "I have no idea what you mean. Please try again."

     def sellStock(self, symbol, share_amt):
        for i in  range(len(self.stockBalance)):
            if self.stockBalance[i]['symbol'] == symbol: 
                num_shares_owned = self.stockBalance[i]['shares']
                stock_to_sell = self.stockBalance[i]['object']
                x = i
        if num_shares_owned >= share_amt:
            stock_to_sell.calc_sell_price()
            total_sell_price = stock_to_sell.sell_price * share_amt
            self.cashBalance += total_sell_price
            self.transactions += "Sold %s shares of %s at a price of $%.2f, for a total of $%.2f.\n" % (share_amt, symbol, stock_to_sell.sell_price, total_sell_price)
            self.stockBalance[x]['shares'] = 0 # this should be num_shares_owned - share_amt
                                               # how do I know if it worked?
 
     def buyMutualFund(self, shares, fund):
        purchase_amount = shares * fund.price
        if (purchase_amount <= self.cashBalance):
            self.cashBalance -= purchase_amount
            self.mfBalance[len(self.mfBalance)] = {"symbol": fund.name, "shares": shares, "object": fund}
            
            self.transactions += ("Purchased %s shares of %s fund at $%.2f per share, for a total of $%.2f.\n" % (shares, fund.name, fund.price, purchase_amount))

        elif (purchase_amount > self.cashBalance):
            return "That purchase exceeds your cash balance of %s. Please enter a smaller purchase." % self.cashBalance

        else: return "I have no idea what you mean. Please try again."

     def sellMutualFund(self, symbol, share_amt):
        for i in  range(len(self.mfBalance)):
            if self.mfBalance[i]['symbol'] == symbol: 
                num_shares_owned = self.mfBalance[i]['shares']
                fund_to_sell = self.mfBalance[i]['object']
                x = i
        if num_shares_owned >= share_amt:
            fund_to_sell.calc_sell_price()
            total_sell_price = fund_to_sell.sell_price * share_amt
            self.cashBalance += total_sell_price
            self.transactions += "Sold %s shares of %s at a price of $%2f, for a total of $%.2f.\n" % (share_amt, symbol, fund_to_sell.sell_price, total_sell_price)
            self.mfBalance[x]['shares'] = 0
            
        else:
            return "You do not have that many shares." 


class Stock(object):
    def __init__(self, price, name):
        self.price = price
        self.name = name
        # make object printable with a def __str__()--see Matthias' code
 
    def calc_sell_price(self):
        self.sell_price = self.price * random.uniform(0.5, 1.5)
        self.sell_price = round(self.sell_price, 2)

class realStock(object):
    def __init__(self, symbol):
        self.price = float(ystockquote.get_price(symbol))
        self.name = symbol
        self.market_cap = ystockquote.get_market_cap(symbol)
        self.ebitda = ystockquote.get_ebitda(symbol)
        self.price_52_week_high = ystockquote.get_52_week_high(symbol)
        self.price_52_week_low = ystockquote.get_52_week_low(symbol)
        self.PE_ratio = ystockquote.get_price_earnings_ratio(symbol)

class MutualFund(object):

    def __init__(self, name):
        self.name = name
        self.price = 1
        
    def calc_sell_price(self):
        self.sell_price = self.price * random.uniform(0.9, 1.2)
        self.sell_price = round(self.sell_price, 2)
        
