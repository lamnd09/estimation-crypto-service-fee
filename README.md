# cryptofee_estimation

This project provides a fee calculation service for crypto and fiat transactions. The service calculates fees based on the crypto network, fiat payment network, customer tier, and liquidity provider availability.

# Project Structure

For this project, I separate the structure into multiple modules. 

* The `services` directory contains the logic for calculating fees and interacting with different services.
* The `models` directory contains the class definitions for `Customer`, `Transaction`, and `Provider`.
* The `utils` directory contains utility functions or classes that don't fit into the other categories.
* File  `main.py` is the entry point of the application. It instantiates the `FeeCalculatorService` and uses it to calculate fees based on user input or predefined data.
* `requirements.txt` lists all the Python packages that the project depends on.

# How to run 



Step 1: Clone this repository.

Step 2: Install the required Python packages with 

```
pip install -r requirements.txt
```

Step 3: Run the `main.py` script with `python main.py`.

Note: Make sure to replace the placeholders in the code with your actual data and API key. 

# Testing
