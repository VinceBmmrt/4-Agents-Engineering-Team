import unittest
from accounts import Account
from unittest.mock import patch

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account('test_user', 1000.0)

    def test_initialization(self):
        self.assertEqual(self.account.username, 'test_user')
        self.assertEqual(self.account.balance, 1000.0)
        self.assertEqual(self.account.holdings, {})
        self.assertEqual(self.account.transactions, [])

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.balance, 1500.0)
        self.assertEqual(len(self.account.transactions), 1)
        self.assertEqual(self.account.transactions[0], 'Deposited: 500.0')

        with self.assertRaises(ValueError):
            self.account.deposit(-100.0)

    def test_withdraw(self):
        self.account.withdraw(300.0)
        self.assertEqual(self.account.balance, 700.0)
        self.assertEqual(len(self.account.transactions), 1)
        self.assertEqual(self.account.transactions[0], 'Withdrew: 300.0')

        with self.assertRaises(ValueError):
            self.account.withdraw(800.0)

        with self.assertRaises(ValueError):
            self.account.withdraw(-100.0)

    @patch('accounts.get_share_price', return_value=150.0)
    def test_buy_shares(self, mock_get_share_price):
        self.account.buy_shares('AAPL', 5)
        self.assertEqual(self.account.balance, 1000.0 - 750.0)
        self.assertEqual(self.account.holdings['AAPL'], 5)
        self.assertEqual(len(self.account.transactions), 1)
        self.assertEqual(self.account.transactions[0], 'Bought 5 shares of AAPL at 150.0 each')

        with self.assertRaises(ValueError):
            self.account.buy_shares('AAPL', 10)

    @patch('accounts.get_share_price', return_value=150.0)
    def test_sell_shares(self, mock_get_share_price):
        self.account.buy_shares('AAPL', 5)
        self.account.sell_shares('AAPL', 3)
        self.assertEqual(self.account.balance, 1000.0 - 750.0 + 450.0)
        self.assertEqual(self.account.holdings['AAPL'], 2)
        self.assertEqual(len(self.account.transactions), 2)
        self.assertEqual(self.account.transactions[1], 'Sold 3 shares of AAPL at 150.0 each')

        with self.assertRaises(ValueError):
            self.account.sell_shares('AAPL', 5)

    @patch('accounts.get_share_price', return_value=150.0)
    def test_get_portfolio_value(self, mock_get_share_price):
        self.account.buy_shares('AAPL', 5)
        self.assertEqual(self.account.get_portfolio_value(), 1000.0 - 750.0)

    def test_get_profit_or_loss(self):
        self.assertEqual(self.account.get_profit_or_loss(), 0.0)
        self.account.deposit(500.0)
        self.assertGreater(self.account.get_profit_or_loss(), 0.0)

    def test_get_holdings(self):
        self.assertEqual(self.account.get_holdings(), {})
        self.account.buy_shares('AAPL', 5)
        self.assertEqual(self.account.get_holdings(), {'AAPL': 5})

    def test_get_transactions(self):
        self.assertEqual(self.account.get_transactions(), [])
        self.account.deposit(500.0)
        self.assertEqual(len(self.account.get_transactions()), 1)

if __name__ == '__main__':
    unittest.main()