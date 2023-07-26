from fee_calculator.services.fee_calculator_service import FeeCalculatorService
from fee_calculator.models.customer import Customer
from fee_calculator.models.transaction import Transaction
from fee_calculator.models.provider import Provider
import json
import pandas as pd
from tabulate import tabulate

# Create some example data
providers = [Provider('Duck', 5), Provider('Goose', 1)]
#transaction = Transaction(100, 'ACH', 'USD', 'ethereum', 'ETH', 'USD')
transactions = [
    Transaction(100, 'ACH', 'USD', 'ethereum', 'ETH', 'USD'),
    Transaction(200, 'ACH', 'USD', 'bitcoin', 'BTC', 'USD'),
    Transaction(150, 'Wire', 'USD', 'ethereum', 'ETH', 'USD'),
    Transaction(500, 'ACH', 'USD', 'bitcoin', 'BTC', 'USD')
]
customer = Customer(1)

# Create the service and calculate the fee
service = FeeCalculatorService(providers)

# Results 
for transaction in transactions:
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


# Present in table
# Initialize lists to store details for all transactions
transaction_details = []
customer_details = []
provider_details = []
fees = []

# Calculate the fee for each transaction
for transaction in transactions:
    fee, provider = service.calculate_fee(transaction, customer)

    # Add details to respective lists
    transaction_details.append(transaction.__dict__)
    customer_details.append(customer.__dict__)
    provider_details.append(provider.__dict__)
    fees.append({
        "Fee": fee,
        "Asset": transaction.fee_asset,
        "Provider": provider.name
    })

# Convert lists to dataframes
transaction_df = pd.DataFrame(transaction_details)
customer_df = pd.DataFrame(customer_details)
providers_df = pd.DataFrame(provider_details)
fees_df = pd.DataFrame(fees)

# Print the tables
print("\n*** Transaction Details ***")
print(tabulate(transaction_df, headers='keys', tablefmt='psql'))

print("\n*** Customer Details ***")
print(tabulate(customer_df, headers='keys', tablefmt='psql'))

print("\n*** Available Providers ***")
print(tabulate(providers_df, headers='keys', tablefmt='psql'))

print("\n*** Fees ***")
print(tabulate(fees_df, headers='keys', tablefmt='psql'))

