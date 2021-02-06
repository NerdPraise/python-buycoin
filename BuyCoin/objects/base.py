from python_graphql_client import GraphqlClient
from requests.exceptions import HTTPError, ConnectionError


from BuyCoin.manager import Manager


class P2PManager(Manager):
    def __init__(self):
        super().__init__()

    def _initialize_client(self):
        auth, data = self._create_request_args()

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
