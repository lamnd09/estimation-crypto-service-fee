from ..models.provider import Provider

class ProviderService:
    def __init__(self, providers):
        self.providers = providers

    def get_fee(self, amount):
        # Store fees from all providers
        fees = []

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
            fees.append(fee)

        # Return the minimum fee among all providers
        return min(fees)

#Testing
# Create some example providers
#providers = [Provider('Duck', 5), Provider('Goose', 10)]

# Create an instance of the ProviderService
#service = ProviderService(providers)
#amount = 100.0
#fee = service.get_fee(amount)

#print(f"The calculated fee for {amount} is {fee}")
