import json
import requests
from dotenv import load_dotenv
import os

class CryptoNetworkService:
    def __init__(self):
        load_dotenv()
        etherscan_apikey = os.getenv('ETHERSCAN_API_KEY')
        self.etherscan_api = f'https://api.etherscan.io/api?module=proxy&action=eth_gasPrice&apikey={etherscan_apikey}'

    def get_fee(self, crypto_network, amount):
        if crypto_network.lower() == 'ethereum':
            fee = self.get_ethereum_fee()
        else:
            fee = self.get_default_fee()  # Note: Other crypto networks can be added here
        return fee

    def get_ethereum_fee(self):
        response = requests.get(self.etherscan_api)
        data = json.loads(response.text)
        gas_price = int(data['result'], 16)  # Note: Convert the hex value to integer
        fee = gas_price / (10 ** 9) * 21000  
        return fee

    def get_default_fee(self):
        return 0.005  # Note: A default fee for unsupported crypto networks

# Testing
# Create an instance of the CryptoNetworkService
#service = CryptoNetworkService()
#crypto_network = 'ethereum'
#amount = 1.0
#fee = service.get_fee(crypto_network, amount)

#print(f"The calculated fee for {amount} {crypto_network} is {fee}")
