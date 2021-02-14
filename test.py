from BuyCoin.objects.wallet import Wallet
from BuyCoin.manager import CustomerWalletManager
from unittest import TestCase


class BuyCoinsTestCase(TestCase):
    def setUp(self):
        pass

    def test_buy_operation(self):
        pass

    def test_sell_operation(self):
        pass

    def test_pnp_operation(self):
        pass

    def tearDown(self):
        pass


d = Wallet(operation="send", cryptocurrency="bitcoin", address="jsdjhshdhsh", coin_amount=0.01)
manager = CustomerWalletManager()
manager.initialize_transaction(d)
