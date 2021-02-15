from unittest import TestCase
from unittest.mock import Mock

from BuyCoin.objects.wallet import Wallet

CustomerWalletManager = Mock()


class WalletTestCase(TestCase):
    buy_response = {"id": "JWhhwqhW&whi32k2o832kmiqwdqb338rP8JIJ9H798fhiidkas=",
                    "cryptocurrency": "bitcoin", "status": "processing", "totalCoinAmount": 0.01, "side": "buy"}
    price_response = {"getPrices": {"buyPricePerCoin": "17164294", "cryptocurrency": "bitcoin",
                                    "id": "QnV5Y29pbnNQcmljZS05NjNmZTExOS02ZGVhLTRlMDItYTc3NC1lZjViYjk3YWZiNGE=",
                                    "maxBuy": "24.90738193", "maxSell": "12.6217372", "minBuy": "0.001",
                                    "minCoinAmount": "0.001", "minSell": "0.001", "sellPricePerCoin": "16824359.1781",
                                    "status": "active"}}

    sell_response = {"id": "JWhhwqhW&738h&whi32k2o832kmiqwdqb338rP8JIJ9H798fhiidka=",
                     "cryptocurrency": "usd_tether", "status": "processing", "totalCoinAmount": 0.01, "side": "sell"}

    address_response = {
        "address": "dgsh663HWhhjHSG&AKSSk22dYDusi8&",
        "cryptocurrency": "usd_coin"
    }

    balance_response = {
        "getBalances": [
            {"id": "wehjwehwa=", "cryptocurrency": "usd_tether", "confirmedBalance": 0.0},
            {"id": "cac23&ahaha", "cryptocurrency": "naira_token", "confirmedBalance": 0.0},
            {"id": "QwehjwehwaWNjb3VudC0=", "cryptocurrency": "bitcoin", "confirmedBalance": 0.02},
            {"id": "wehjwehwasa323", "cryptocurrency": "ethereum", "confirmedBalance": 1.0},
            {"id": "QWNjb3VudC0=", "cryptocurrency": "litecoin", "confirmedBalance": 0.0},
            {"id": "QWNjb3VudC0=", "cryptocurrency": "usd_coin", "confirmedBalance": 0.0}
        ]
    }

    def setUp(self):
        CustomerWalletManager = Mock()

    def test_can_sell_crypto(self):
        sale_order = Wallet(operation="sell", cryptocurrency="usd_tether", coin_amount=0.01)

        CustomerWalletManager.initialize_transaction.return_value = self.sell_response
        response = CustomerWalletManager.initialize_transaction(sale_order)
        self.assertEqual(response["side"], "sell")
        self.assertEqual(response["totalCoinAmount"], 0.01)
        self.assertEqual(response["cryptocurrency"], "usd_tether")

    def test_can_buy_crypto(self):
        sale_order = Wallet(operation="buy", cryptocurrency="bitcoin", coin_amount=0.2)

        CustomerWalletManager.initialize_transaction.return_value = self.buy_response
        response = CustomerWalletManager.initialize_transaction(sale_order)
        self.assertEqual(response["side"], "buy")
        self.assertEqual(response["totalCoinAmount"], 0.01)
        self.assertEqual(response["cryptocurrency"], "bitcoin")

    def test_can_create_address(self):
        create_address_order = Wallet(operation="create", cryptocurrency="usd_coin",
                                      address="dgsh663HWhhjHSG&AKSSk22dYDusi8&")

        CustomerWalletManager.initialize_transaction.return_value = self.address_response
        response = CustomerWalletManager.initialize_transaction(create_address_order)
        self.assertEqual(response["address"], "dgsh663HWhhjHSG&AKSSk22dYDusi8&")
        self.assertEqual(response["cryptocurrency"], "usd_coin")

    def test_get_balance(self):
        balance_order = Wallet(operation="balance", cryptocurrency="usd_coin")

        CustomerWalletManager.initialize_transaction.return_value = self.balance_response
        response = CustomerWalletManager.initialize_transaction(balance_order)
        self.assertEqual(response["getBalances"][2]["id"], "QwehjwehwaWNjb3VudC0=")
        self.assertEqual(response["getBalances"][2]["confirmedBalance"], 0.02)
        self.assertEqual(response["getBalances"][2]["cryptocurrency"], "bitcoin")

    def test_can_get_prices(self):
        CustomerWalletManager.get_prices.return_value = self.price_response

        response = CustomerWalletManager.get_prices(cryptocurrency="bitcoin")
        self.assertEqual(response["getPrices"]["id"],
                         "QnV5Y29pbnNQcmljZS05NjNmZTExOS02ZGVhLTRlMDItYTc3NC1lZjViYjk3YWZiNGE=")
        self.assertEqual(response["getPrices"]["cryptocurrency"], "bitcoin")
        self.assertEqual(response["getPrices"]["buyPricePerCoin"], "17164294")
