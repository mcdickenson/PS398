require_relative "invest"

port = Portfolio.new()
port.print

port.addCash(300.50)
port.print


s = Stock.new(20, "HFH")
s.print

port.buyStock(5, s)
port.print

mf1 = MutualFund.new("BRT")
mf1.print
mf2 = MutualFund.new("GHT")
mf2.print
port.buyMutualFund(10.3, mf1)
port.print
port.buyMutualFund(2, mf2)
port.print

port.sellStock("HFH", 1)
port.print

port.sellMutualFund("BRT", 3)
port.print

port.withdrawCash(50)
port.print

puts "History of this portfolio..."
port.history
