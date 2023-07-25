from .crypto_network_service import CryptoNetworkService
from .fiat_network_service import FiatNetworkService
from .provider_service import ProviderService
from ..utils.discount_calculator import DiscountCalculator

class FeeCalculatorService:
    def __init__(self, providers):
        self.providers = providers
        self.crypto_service = CryptoNetworkService()
        self.fiat_service = FiatNetworkService()
        self.provider_service = ProviderService(providers)
        self.discount_calculator = DiscountCalculator()

    def calculate_fee(self, transaction, customer):
        crypto_fee = self.crypto_service.get_fee(transaction.to_network, transaction.from_amount)
        fiat_fee = self.fiat_service.get_fee(transaction.from_network, transaction.from_amount)
        provider_fee = self.provider_service.get_fee(transaction.from_amount)
        
        total_fee = crypto_fee + fiat_fee + provider_fee
        total_fee = self.discount_calculator.apply_discounts(customer, total_fee, crypto_fee, fiat_fee)
        
        return total_fee
