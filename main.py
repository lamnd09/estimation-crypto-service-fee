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
fee = service.calculate_fee(transaction, customer)

# Log the inputs and outputs
print("Service Input:")
print("// Transaction")
print(json.dumps(transaction.__dict__, indent=2))

print("// Customer")
print(json.dumps(customer.__dict__, indent=2))

print("// AvailableProviders")
print(json.dumps([provider.__dict__ for provider in providers], indent=2))

print("\nExample Service Output:")
print("// Fees")
output = {
    "Fee": fee,
    "Asset": transaction.fee_asset,
    "Provider": "Goose"  # You'll need to modify your FeeCalculatorService to return the provider with the lowest fee
}
print(json.dumps(output, indent=2))
