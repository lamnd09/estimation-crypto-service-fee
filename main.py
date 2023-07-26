from fee_calculator.services.fee_calculator_service import FeeCalculatorService
from fee_calculator.models.customer import Customer
from fee_calculator.models.transaction import Transaction
from fee_calculator.models.provider import Provider
import json

# Create some example data
providers = [Provider('Duck', 5), Provider('Goose', 10)]
transaction = Transaction(100, 'ACH', 'USD', 'ethereum', 'ETH', 'USD')
customer = Customer(1)

# Create the service and calculate the fee
service = FeeCalculatorService(providers)
fee, provider = service.calculate_fee(transaction, customer)

# Log the inputs and outputs
print("\n *** Transaction Detail ***")
print(json.dumps(transaction.__dict__, indent=2))

print("\n *** Customer ***")
print(json.dumps(customer.__dict__, indent=2))

print("\n *** AvailableProviders *** ")
print(json.dumps([provider.__dict__ for provider in providers], indent=2))

print("\n *** Fees ***")
output = {
    "Fee": fee,
    "Asset": transaction.fee_asset,
    "Provider": provider.to_dict()  
    }
print(json.dumps(output, indent=2))
