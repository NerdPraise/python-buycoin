from unittest import TestCase
from unittest.mock import Mock

from BuyCoin.objects.p2p import P2P

P2PManager = Mock()


class P2PTestCase(TestCase):
    plo_response = dict(
        id="UG9zdE9yZGVyLTgwY2M3MjdmLWQzYjEtNDE0OS04MDg3LTJkNjI0MDdhMWMzMw",
        cryptocurrency="bitcoin",
        coinAmount=1.0,
        side="buy",
        status="inactive",
        createdAt=1612307038,
        pricePerCoin="16000000.0",
        priceType="static",
        staticPrice="16000000",
        dynamicExchangeRate=None,
    )

    pmo_response = {
        "id": "UG9zdE9yZGVyLTgwY2M3MjdmLWQzYjEtNDE0OS04MDg3LTJkNjI0MDdhMWMzMw",
        "cryptocurrency": "bitcoin",
        "coinAmount": 0.01,
        "side": "buy",
        "status": "inactive",
        "createdAt": 1612307038,
        "pricePerCoin": "16000000.0",
        "priceTy    pe": None,
        "staticPrice": None,
        "dynamicExchangeRate": None}

    def setUp(self):
        P2PManager = Mock()

    def test_can_place_market_order(self):
        sale_order = P2P(operation="pmo", cryptocurrency="usd_tether", side="buy", coin_amount=0.01)

        P2PManager.initialize_transaction.return_value = self.pmo_response
        response = P2PManager.initialize_transaction(sale_order)
        self.assertTrue(response["id"], "UG9zdE9yZGVyLTgwY2M3MjdmLWQzYjEtNDE0OS04MDg3LTJkNjI0MDdhMWMzMw")
        self.assertTrue(response["cryptocurrency"], "bitcoin")
        self.assertTrue(response["coinAmount"], 0.01)
        self.assertTrue(response["side"], "sell")
        self.assertTrue(response["status"], "inactive")
