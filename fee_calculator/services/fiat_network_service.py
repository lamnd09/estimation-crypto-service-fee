class FiatNetworkService:
    def get_fee(self, fiat_network, amount):
        if fiat_network.lower() == 'ach':
            fee = max(2, amount * 0.01)  # $2 or 1% of amount, whichever is higher
        elif fiat_network.lower() == 'wire':
            fee = 25  # flat $25 fee
        elif fiat_network.lower() == 'card':
            fee = amount * 0.03  # 3% of amount
        else:
            fee = 0  # If the fiat network is not recognized, return 0 fee
        return fee

#Testing
# Create an instance of the FiatNetworkService
#service = FiatNetworkService()
#fiat_network = 'ach'
#amount = 100.0
#fee = service.get_fee(fiat_network, amount)

#print(f"The calculated fee for {amount} {fiat_network} is {fee}")
