""" Homework 2
Computational Frameworks, POLS 398
Spring 2012, Duke University
Matt Dickenson """

import random

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
        # TODO: make this print nicely as in the HW assignment

     def history(self):
        print self.transactions
     
     def addCash(self, amount):
        self.cashBalance += amount
        self.transactions += ("$%s added.\n" % amount)

     def withdrawCash(self, amount):
        self.cashBalance -= amount
        self.transactions += ("$%s withdrawn. \n" % amount)

     def buyStock(self, shares, stock):
        purchase_amount = shares * stock.price
        if (shares % 1 == 0) & (purchase_amount <= self.cashBalance):
            self.cashBalance -= purchase_amount
            self.stockBalance[len(self.stockBalance)] = {"symbol": stock.name, "shares": shares, "object": stock}
            
            self.transactions += ("Purchased %s shares of %s stock at $%s per share, for a total of $%s.\n" % (shares, stock.name, stock.price, purchase_amount))

        elif (shares % 1 == 0) & (purchase_amount > self.cashBalance):
            return "That purchase exceeds your cash balance of %s. Please enter a smaller purchase." % self.cashBalance

        elif (shares % 1 != 0):
            return "Fractional shares cannot be purchased. Please enter a whole number of shares."

        else: return "I have no idea what you mean. Please try again."

     def sellStock(self, stock, shares):
        pass
        # see sellMutualFund
     
     def buyMutualFund(self, shares, fund):
        purchase_amount = shares * fund.price
        if (purchase_amount <= self.cashBalance):
            self.cashBalance -= purchase_amount
            self.mfBalance.append([shares, fund.name])
            self.transactions += ("Purchased %s shares of %s fund at %s per share, for a total of %s.\n" % (shares, fund.name, fund.price, purchase_amount))

        elif (purchase_amount > self.cashBalance):
            return "That purchase exceeds your cash balance of %s. Please enter a smaller purchase." % self.cashBalance

        else: return "I have no idea what you mean. Please try again."

     def sellMutualFund(self, symbol, share_amt):
        pass
        # look up the fund in the mf dict
        # make sure you own at least as many shares as share_amt
        # calculate the fund's selling price
        # cashBalance += fund_name.sell_price * share_amt

class Asset(object):

    def __init__(self, price, name):
        self.price = price
        self.name = name

    def buy(self, shares, title): 
        if self.check_fraction(shares) == True:
            self.check_purchase(shares)

    def check_purchase(self, shares, title):
        if shares * self.
    


class Stock(Asset):

    def check_fraction(self, shares):
        if shares % 1 == 0: return True
        
    def calc_sell_price(self):
        self.sell_price = self.price * random.uniform(0.5, 1.5)

class MutualFund(Asset):

    def check_fraction(self):
        return True
        
    def calc_sell_price(self):
        self.sell_price = self.price * random.uniform(0.9, 1.2)
