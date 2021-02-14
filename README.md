# Python-buycoin

A python SDK for BuyCoins
#### Update
New features to be added to SDK includes
1. Type hinting
2. NGNT manager and transactions

## Installations
```shell
pip install python-buycoins
```
## Requirements
Python 3.0+

## Documentation
You can view the official documentation for the BuyCoins APi can be found [here](https://https//developers.buycoins.africa/) on the BuyCoins developer portal.


## Configuration
Create a .env file and set up authentication as follows:
```
BUYCOIN_PUBLIC_KEY="<BUYCOIN_PUBLIC_KEY>"
BUYCOIN_SECRET_KEY="<BUYCOIN_SECRET_KEY>"
```
To get public and private key, follow the process set at [here](https://developers.buycoins.africa/#how-do-i-get-access)

## Usage
Most of the library's functionality lies in the managers.py file which contains all the managers required to perform wallet transactions, peer to peer transactions and NGNT transactions.

The Manager classes handle every direct interaction with the BuyCoins API.

### Wallet Transactions
This involves direct purchase, sale, transfer orders of cryptocurrencies and creation of cryptocurrencies addresses
A sample use-case

```Python
from BuyCoin.objects.wallet import Wallet
from BuyCoin.manager import CustomerWalletManager

# Start a  purchase transaction and then assign to manager for initialization
purchase_order = Wallet(operation="buy", cryptocurrency="bitcoin", coin_amount=0.01)
wallet_manager = CustomerWalletManager()
wallet_manager.initialize_transaction(purchase_order)

# To get prices for all cryptocurrencies
print(wallet_manager.get_prices())

# To get prices for a specific cryptocurrency for a side ('buy', 'sell')
print(wallet_manager.get_prices(cryptocurrency="bitcoin", side="buy"))
```