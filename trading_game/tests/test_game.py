import unittest
from trading_game.market import Market
from trading_game.game import Player

class PlayerTestCase(unittest.TestCase):
    def setUp(self):
        self.market = Market()
        self.player = Player()

    def test_buy_stock(self):
        price = self.market.get_price('AAPL')
        success = self.player.buy('AAPL', 1, self.market)
        self.assertTrue(success)
        self.assertEqual(self.player.portfolio.get('AAPL'), 1)
        self.assertAlmostEqual(self.player.cash, 1000.0 - price)

    def test_sell_stock(self):
        self.player.portfolio['AAPL'] = 2
        price = self.market.get_price('AAPL')
        success = self.player.sell('AAPL', 1, self.market)
        self.assertTrue(success)
        self.assertEqual(self.player.portfolio.get('AAPL'), 1)
        self.assertAlmostEqual(self.player.cash, 1000.0 + price)

if __name__ == '__main__':
    unittest.main()
