from python_graphql_client import GraphqlClient
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError, ConnectionError


from config import BuyCoinConfig


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

    def _initialize_client(self):
        """
        Create GraphQL client for executing queries
        Returns client
        """
        auth = self._create_request_args()

        try:
            self._client = GraphqlClient(endpoint=self.BUYCOIN_URL, auth=auth)
        except (HTTPError, ConnectionError) as e:
            return e
        else:
            return self._client

    def _perform_request(self, query, variables):
        if not query:
            pass
        try:
            self._client.execute(query=query, variables=variables)
        except (ConnectionError, HTTPError) as e:
            return e


class P2PManager(Manager):
    pass


class WalletManager(Manager):
    pass


class NGNTManager(Manager):
    pass
