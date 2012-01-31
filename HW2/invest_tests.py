# /Users/mcdickenson/github/PS398/HW2/
import unittest
import invest

class TestInvestCode(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.portfolio = invest.Portfolio()
        self.s = invest.Stock(20, "HFH")
        self.mf1 = invest.MutualFund("BRT")
        self.mf2 = invest.MutualFund("GHT")

    # correctness tests:

    def test_create_portfolio(self):
        self.assertIsInstance(self.portfolio, invest.Portfolio)

    def test_add_cash(self):
        self.portfolio.addCash(300.50)
        self.assertEqual(self.portfolio.cashBalance, 300.50)


    def test_create_stock(self):
        self.assertEqual(self.s.price, 20)
        self.assertEqual(self.s.name, "HFH")

    def test_buy_stock(self):
        self.portfolio.cashBalance = 300.50
        self.portfolio.buyStock(5, self.s)
        self.assertEqual(self.portfolio.cashBalance, 200.50)

    def test_create_mutual_fund1(self):
        self.assertIsInstance(self.mf1, invest.MutualFund)
        self.assertEqual(self.mf1.price, 1)
        self.assertEqual(self.mf1.name, "BRT")

    def test_create_mutual_fund2(self):   
        self.assertIsInstance(self.mf2, invest.MutualFund)
        self.assertEqual(self.mf2.price, 1)
        self.assertEqual(self.mf2.name, "GHT")   
            
    def test_buy_mutual_fund(self):
        self.portfolio.cashBalance = 200.50
        self.portfolio.buyMutualFund(2, self.mf2)
        self.assertEqual(self.portfolio.cashBalance, 198.50)

    def test_sell_mutual_fund(self):
        self.portfolio.cashBalance = 100
        self.portfolio.buyMutualFund(10, self.mf1)
        self.portfolio.sellMutualFund("BRT", 3)
        self.assertNotEqual(self.portfolio.cashBalance, 90)

    def test_sell_stock(self):
        self.portfolio.cashBalance = 100
        self.portfolio.buyStock(5, self.s)
        self.portfolio.sellStock("HFH", 1)
        self.assertNotEqual(self.portfolio.cashBalance, 0)

    def test_withdraw_cash(self):
        self.portfolio.cashBalance = 100
        self.portfolio.withdrawCash(50)
        self.assertEqual(self.portfolio.cashBalance, 50)

    def test_portfolio_history(self):   
        self.portfolio.addCash(300.50)
        self.assertEqual(self.portfolio.transactions, "$300.50 added.\n")

    def test_portfolio_history2(self):   
        self.portfolio.addCash(300.50)
        self.portfolio.buyStock(5, self.s)
        self.assertEqual(self.portfolio.transactions, "$300.50 added.\nPurchased 5 shares of HFH stock at $20.00 per share, for a total of $100.00.\n")

    def test_buy_real_stock(self):
        self.portfolio.cashBalance = 1000
        self.google = invest.realStock('GOOG')
        self.portfolio.buyStock(1, self.google)
        self.assertEqual(self.portfolio.stockBalance[0]['shares'], 1)
        
    def test_buy_real_stock2(self):
	    self.portfolio.cashBalance = 1000
	    self.google = invest.realStock('GOOG')
	    self.portfolio.buyStock(1, self.google)
	    self.assertNotEqual(self.portfolio.cashBalance, 1000)

    # robustness tests: 

    def test_fractional_mf_purchase(self):
        self.portfolio.cashBalance = 300
        self.assertEqual(self.portfolio.buyMutualFund(10.3, self.mf1), None)

    def test_fractional_stock_purchase(self):
        self.portfolio.cashBalance = 300
        self.assertEqual(self.portfolio.buyStock(10.3, self.s), "Fractional shares cannot be purchased. Please enter a whole number of shares.")

   


if __name__ == '__main__':
    unittest.main()
