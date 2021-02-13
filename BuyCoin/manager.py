from python_graphql_client import GraphqlClient
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError, ConnectionError
import json
import jsonpickle


from config import BuyCoinConfig
from BuyCoin.objects.errors import QueryError


class Manager:
    """
    Abstract Base Class
    """
    BUYCOIN_URL = None
    USERNAME = None
    PASSWORD = None

    def __init__(self):
        super().__init__()
        if type(self) is Manager:
            raise TypeError("Can not make instance of abstract base class")

        if not BuyCoinConfig.BUYCOIN_SECRET_KEY or not BuyCoinConfig.BUYCOIN_PUBLIC_KEY:
            raise ValueError("No secret key or public key found, \
                             assign values using BuyCoinConfig.BUYCOIN_PUBLIC_KEY = SECRET_KEY and \
                             BuyCoinConfig.BUYCOIN_PUBLIC_KEY = PUBLIC_KEY")

        self.USERNAME = BuyCoinConfig.BUYCOIN_PUBLIC_KEY
        self.PASSWORD = BuyCoinConfig.BUYCOIN_SECRET_KEY
        self.BUYCOIN_URL = BuyCoinConfig.BUYCOIN_URL

    def _create_request_args(self):
        """
        Returns required headers
        """
        auth = HTTPBasicAuth(self._username, self._password)

        return auth

    def to_json(self, data, pickled=False):
        '''
        Method to serialize class instance
        '''
        if pickled:
            return jsonpickle.encode(data)
        else:
            data = json.JSONDecoder().decode(jsonpickle.encode(data))
            data.pop("py/object")
            return data

    def _initialize_client(self):
        """
        Create GraphQL client for executing queries
        Returns client
        """
        auth = self._create_request_args()

        try:
            _client = GraphqlClient(endpoint=self.BUYCOIN_URL, auth=auth)
        except (HTTPError, ConnectionError) as e:
            return e
        else:
            return _client

    def _perform_request(self, query, variables={}):
        self._client = self._initialize_client()
        if not query:
            return QueryError('Invalid Query')
        try:
            request = self._client.execute(query=query, variables=variables)
        except (ConnectionError, HTTPError) as e:
            return e
        except QueryError as e:
            return e.response
        else:
            return request


class P2PManager(Manager):
    pass


class CustomerWalletManager(Manager):
    """
    Manager handles every transaction concerning cryptocurrency
    Includes buying, selling, getting prices, creating addresses and getting crypto-balance

    """
    _BUY_QUERY = """
        mutation BuyCoin($price: ID!, $coin_amount: BigDecimal!, $cryptocurrency: Cryptocurrency){
                buy(price: $price, coin_amount: $coin_amount, cryptocurrency: $cryptocurrency) {
                    id
                    cryptocurrency
                    status
                    totalCoinAmount
                    side
                }
            }
        """
    _SELL_QUERY = """
        mutation SellCoin($price: ID!, $coin_amount: BigDecimal!, $currency: Cryptocurrency){
            sell(price: $price, coin_amount: $coin_amount, cryptocurrency: $currency) {
                id
                cryptocurrency
                status
                totalCoinAmount
                side
            }
        }

    """

    _GET_PRICE_QUERY = """
        query {
            getPrices {
                id
                cryptocurrency
                buyPricePerCoin
                minBuy
                maxBuy
                expiresAt
            }
        }
        """
    _GET_CRYPTO_PRICE_QUERY = """
        query GetBuyCoinsPrices($cryptocurrency: Cryptocurrency) {
            getPrices(cryptocurrency: $cryptocurrency){
                buyPricePerCoin
                cryptocurrency
                id
                maxBuy
                maxSell
                minBuy
                minCoinAmount
                minSell
                sellPricePerCoin
                status
            }
        }
    """

    _CREATE_ADDRESS = """
        mutation CreateWalletAddress($cryptocurrency: Cryptocurrency) {
            createAddress(cryptocurrency: $cryptocurrency) {
                cryptocurrency
                address
            }
        }
    """

    def __init__(self):
        super().__init__()

    def get_prices(self, cryptocurrency=None):
        """
        Retrieve all cryptocurrencies current price

        Args:
            cryptocurrency: Retrieve specific cryptocurrency price

        Returns:
            response: a list of cryptocurrency and their prices
        """
        if cryptocurrency:
            query = self._GET_CRYPTO_PRICE_QUERY
            variables = {
                "cryptocurrency": cryptocurrency
            }
        else:
            query = self._GET_PRICE_QUERY
            variables = {}

        try:
            response = self._perform_request(query=query, variables=variables)
        except Exception as e:
            raise e
        else:
            return response["data"]["getPrices"]

    def initialize_transaction(self, wallet_transaction):
        data = self.to_json(wallet_transaction)
        operation = data.pop("operation")
        variables = {**data}

        if operation == "buy":
            query = self._BUY_QUERY
            price = self.get_prices(cryptocurrency=data["cryptocurrency"])
            variables = {**variables, "price": price[0]["id"]}
        elif operation == "sell":
            query = self._SELL_QUERY
            price = self.get_prices(cryptocurrency=data["cryptocurrency"])
            variables = {**variables, "price": price[0]["id"]}
        elif operation == "create":
            query = self._CREATE_ADDRESS
        elif operation == "balance":
            pass

        try:
            response = self._perform_request(query=query, variables=variables)
        except Exception as e:
            raise e
        else:
            return response["data"]


class NGNTManager(Manager):
    pass
