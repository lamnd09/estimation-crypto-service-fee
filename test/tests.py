import pytest
from fee_calculator.services.crypto_network_service import CryptoNetworkService
from fee_calculator.services.fiat_network_service import FiatNetworkService
from fee_calculator.services.fee_calculator_service import FeeCalculatorService
from fee_calculator.services.provider_service import ProviderService
from fee_calculator.models.transaction import Transaction
from fee_calculator.models.customer import Customer
from fee_calculator.models.provider import Provider
from fee_calculator.utils.discount_calculator import DiscountCalculator

# CryptoNetworkService tests
def test_crypto_get_fee():
    service = CryptoNetworkService()
    fee = service.get_fee('ethereum', 1.0)
    assert isinstance(fee, float)

# FiatNetworkService tests
def test_fiat_get_fee():
    service = FiatNetworkService()
    fee = service.get_fee('ACH', 100.0)
    assert isinstance(fee, (int, float))

# FeeCalculatorService tests
def test_calculate_fee():
    providers = [Provider('Duck', 5), Provider('Goose', 10)]
    service = FeeCalculatorService(providers)
    transaction = Transaction(100, 'ACH', 'USD', 'ethereum', 'ETH', 'USD')
    customer = Customer(1)
    fee, provider = service.calculate_fee(transaction, customer)
    assert isinstance(fee, float)

# ProviderService tests
def test_provider_get_fee():
    providers = [Provider('Duck', 5), Provider('Goose', 10)]
    service = ProviderService(providers)
    provider, fee = service.get_lowest_fee(100.0)
    assert isinstance(fee, float)

# DiscountCalculator tests
def test_apply_discounts():
    calculator = DiscountCalculator()
    customer = Customer(1)
    total_fee = 10.0
    crypto_fee = 5.0
    fiat_fee = 2.0
    discounted_fee = calculator.apply_discounts(customer, total_fee, crypto_fee, fiat_fee)
    assert isinstance(discounted_fee, float)
