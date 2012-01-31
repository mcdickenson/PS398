import invest

portfolio=invest.Portfolio()
print(portfolio)
portfolio.history()

portfolio.addCash(300.50)
print(portfolio)
portfolio.history()

portfolio.withdrawCash(50)
portfolio.history()
print(portfolio)

s = invest.Stock(20 , "HFH")
s.name
s.price 
portfolio.buyStock(5, s) 
portfolio.history() 
print(portfolio) 

mf1 = invest.MutualFund(5, "BRT")
mf1.name
mf1.price

mf2 = invest.MutualFund (2, "GHT")
mf2.price
mf2.name

portfolio.buyMutualFund(10.3 , mf1)
print(portfolio)
portfolio.history()

portfolio.buyMutualFund (2, mf2)
print(portfolio)
portfolio.history()

portfolio.sellMutualFund("BRT", 3)
portfolio.history()
print(portfolio)

portfolio.sellStock("HFH", 1)
portfolio.history()
print(portfolio)

# check math at each stage
# then run real tests
