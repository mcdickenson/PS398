# /Users/mcdickenson/github/PS398/HW2/
import unittest
import invest

class TestInvestCode(unittest.TestCase):

    def setUp(self):
        return

    # correctness tests:

    def test_create_portfolio(self):
        portfolio = invest.Portfolio()
        self.assertIsInstance(portfolio, invest.Portfolio)

    def test_add_cash(self):
        portfolio.addCash(300.50)
        self.assertEqual(portfolio.cashBalance, 300.50)


    def test_create_stock(self):
        s = invest.Stock(20, "HFH")
        self.assertEqual(s.price, 20)
        self.assertEqual(s.symbol, "HFH")

    def test_buy_stock(self):
        portfolio.invest.buyStock(5, 2)
        self.assertEqual(portfolio.cashBalance, 200.50)
        #self.assertEqual(portfolio.Stock, 100)

    def test_create_mutual_fund1(self):
        mf1 = invest.MutualFund("BRT")
        self.assertIsInstance(mf1, invest.MutualFund)
        self.assertEqual(mf1.price, 1)
        self.assertEqual(mf1.symbol, "BRT")

    def test_create_mutual_fund2(self):
        mf2 = invest.MutualFund("GHT")
        self.assertIsInstance(mf2, invest.MutualFund)
        self.assertEqual(mf1.price, 1)
        self.assertEqual(mf1.symbol, "GHT")   
            
    def test_buy_mutual_fund(self):
        portfolio.invest.buyMutualFund(2, mf2)
        self.assertEqual(portfolio.Cash, 198.50)
        # self.assertEqual(portfolio.MutualFund, 4) # may chg to MutualFundValue

    def test_print_portfolio(self):
        print(portfolio) # NOT DONE

    def test_sell_mutual_fund(self):
        pass

    def test_sell_stock(self):
        pass

    def test_withdraw_cash(self):
        pass

    def test_portfolio_history(self):   
        pass
	

    # robustness tests: 

    def test_fractional_stock_purchase(self):
        assertEqual(portfolio.invest.buyMutualFund(10.3, mf1), "Fractional shares not allowed.")

   


if __name__ == '__main__':
    unittest.main()
