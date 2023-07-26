# Estimation Service Fee On/Off-ramp product

This project provides a fee calculation service for crypto and fiat transactions. The service calculates fees based on the crypto network, fiat payment network, customer tier, and liquidity provider availability.

# 1. Project Structure

For this project, I separate the structure into multiple modules.

* The `services` directory contains the logic for calculating fees and interacting with different services.
* The `models` directory contains the class definitions for `Customer`, `Transaction`, and `Provider`.
* The `utils` directory contains utility functions or classes
* File  `main.py` is the entry point of the application. It instantiates the `FeeCalculatorService` and uses it to calculate fees based on user input or predefined data.
* The `test` folder for test cases
* `requirements.txt` lists all the Python packages that the project depends on.

# 2. How to run

Step 1: Clone this repository.

Update .env with your personal etherscan API KEY

Step 2: Install the required Python packages with

```
pip install -r requirements.txt
```

Step 3: Run the `main.py` script with

```
python main.py
```

Note: Make sure to replace the placeholders in the code with your actual data and API key.

The output could be:

```
 *** Transaction Detail ***
{
  "from_amount": 200,
  "from_network": "ACH",
  "from_asset": "USD",
  "to_network": "bitcoin",
  "to_asset": "BTC",
  "fee_asset": "USD"
} *** Customer ***
{
  "tier": 1
}

*** AvailableProviders ***
[
  {
    "name": "Duck",
    "fee": 5
  },
  {
    "name": "Goose",
    "fee": 1
  }

*** Fees ***
{
  "Fee": 2.605,
  "Asset": "USD",
  "Provider": {
    "name": "Goose",
    "fee": 1
  }
}
```

# 3. Testing

Run the test for the features:

```
pytest -s -v tests.py

tests.py::test_crypto_get_fee PASSED
tests.py::test_fiat_get_fee PASSED
tests.py::test_calculate_fee PASSED
tests.py::test_provider_get_fee PASSED
tests.py::test_apply_discounts PASSED

======================== 5 passed in 2.50s =====================
```

# References

[1] Etherscan API:  https://etherscan.io/apis

[2] Coingecko API: https://www.coingecko.com/en/api/documentation
