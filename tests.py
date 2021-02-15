# from BuyCoin.objects.wallet import Wallet
from BuyCoin.objects.p2p import P2P
from BuyCoin.manager import CustomerWalletManager, P2PManager
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


# d = Wallet(operation="send", cryptocurrency="bitcoin", address="jsdjhshdhsh", coin_amount=0.01)
d = P2P(side="buy", coin_amount=0.01, cryptocurrency="bitcoin",
        operation="plo", price_type="dynamic", dynamic_exchange_rate=3000)
manager = P2PManager()
manager.initialize_transaction(d)
