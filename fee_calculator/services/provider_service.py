
from ..models.provider import Provider

class ProviderService:
    def __init__(self, providers):
        self.providers = providers

    def get_lowest_fee(self, amount):
        fees = {}

        # Calculate fee for each provider
        for provider in self.providers:
            if provider.name.lower() == 'duck':
                fee = 5 + 0.001 * amount  # $5 + 0.1% of the trade amount
            elif provider.name.lower() == 'goose':
                fee = 0.003 * amount  # 0.3% of the trade amount
            elif provider.name.lower() == 'fox':
                fee = 0.005 * amount  # 0.5% of the trade amount
            else:
                fee = float('inf')  # If the provider is not recognized, set the fee to infinity

            fees[provider] = fee

        # Return the provider with the minimum fee and the fee
        min_provider = min(fees, key=fees.get)
        print(min_provider)
        return min_provider, fees[min_provider]


#Testing
#Create some example providers
#providers = [Provider('Duck', 5), Provider('Goose', 1)]
#service = ProviderService(providers)
#mount = 100.0
#fee = service.get_lowest_fee(amount)
#print("The calculated fee for", amount," is ", fee)
