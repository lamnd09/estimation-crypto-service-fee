import requests
import json

class CryptoNetworkService:
    def __init__(self):
        self.etherscan_api = 'https://api.etherscan.io/api?module=proxy&action=eth_gasPrice&apikey=7QV79BZ4RTRC75HU3W5AH9P7CDXR3HUI3Y'

    def get_fee(self, crypto_network, amount):
        if crypto_network.lower() == 'ethereum':
            fee = self.get_ethereum_fee()
        else:
            fee = self.get_default_fee()  # Other crypto networks can be added here
        return fee

    def get_ethereum_fee(self):
        response = requests.get(self.etherscan_api)
        data = json.loads(response.text)
        gas_price = int(data['result'], 16)  # Convert the hex value to integer
        fee = gas_price / (10 ** 9) * 21000  
        return fee

    def get_default_fee(self):
        return 0.005  # A default fee for unsupported crypto networks

# Testing
# Create an instance of the CryptoNetworkService
service = CryptoNetworkService()
crypto_network = 'ethereum'
amount = 1.0
fee = service.get_fee(crypto_network, amount)

print(f"The calculated fee for {amount} {crypto_network} is {fee}")
