import unittest
import HW2

class TestHW2Code(unittest.TestCase):

    def setUp(self):
        return

    # correctness tests:

    def test_create_portfolio(self):
        try:
            portfolio = HW2.Portfolio()
            self.assertIsInstance(portfolio, HW2.Portfolio)

    def test_add_cash(self):
        try:
            portfolio.HW2.addCash(300.50)
            self.assertEqual(portfolio.Cash, 300.50)


    def test_create_stock(self):
        try:
            s = HW2.Stock(20, "HFH")
            self.assertEqual(s.price, 20)
            self.assertEqual(s.symbol, "HFH")

    def test_buy_stock(self):
        try: 
            portfolio.HW2.buyStock(5, 2)
            self.assertEqual(portfolio.Cash, 200.50)
            self.assertEqual(portfolio.Stock, 100)

    def test_create_mutual_fund1(self):
        try:
            mf1 = HW2.MutualFund(5, "BRT")
            self.assertIsInstance(mf1, HW2.MutualFund)
            self.assertEqual(mf1.price, 5)
            self.assertEqual(mf1.symbol, "BRT")

    def test_create_mutual_fund2(self):
        try:
            mf2 = HW2.MutualFund(2, "GHT")
            self.assertIsInstance(mf2, HW2.MutualFund)
            self.assertEqual(mf1.price, 2)
            self.assertEqual(mf1.symbol, "GHT")   
            
    def test_buy_mutual_fund(self):
        try: 
            portfolio.HW2.buyMutualFund(2, mf2)
            self.assertEqual(portfolio.Cash, 196.50)
            self.assertEqual(portfolio.MutualFund, 4) # may chg to MutualFundValue

    def test_print_portfolio(self):
        try:
            print(portfolio) # NOT DONE

    def test_sell_mutual_fund(self):

    def test_sell_stock(self):

    def test_withdraw_cash(self):

    def test_portfolio_history(self):   
	

    # robustness tests: 

    def test_fractional_stock_purchase(self):
        try:
            assertEqual(portfolio.HW2.buyMutualFund(10.3, mf1), "Fractional shares not allowed.")

   


if __name__ == '__main__':
    unittest.main()
