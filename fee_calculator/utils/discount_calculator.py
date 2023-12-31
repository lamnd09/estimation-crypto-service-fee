from ..models.customer import Customer

class DiscountCalculator:
    def apply_discounts(self, customer, total_fee, crypto_fee, fiat_fee):
        if customer.tier == 1:
            # Tier 1: No discount
            discounted_fee = total_fee

        elif customer.tier == 2:
            # Tier 2: 25% discount on crypto fee + 25% discount on fiat payment network
            discounted_fee = total_fee - 0.25 * (crypto_fee + fiat_fee)

        elif customer.tier == 3:
            # Tier 3: 50% discount on crypto fee, except Ethereum (still 25%) 
            # + 100% discount on fiat payment network except Wire (still 25%)
            if customer.crypto_network.lower() == 'ethereum':
                discounted_fee = total_fee - 0.25 * crypto_fee
            else:
                discounted_fee = total_fee - 0.50 * crypto_fee

            if customer.fiat_network.lower() == 'wire':
                discounted_fee = discounted_fee - 0.25 * fiat_fee
            else:
                discounted_fee = discounted_fee - fiat_fee  # 100% discount

        else:
            # If the tier is not recognized, no discount is applied
            discounted_fee = total_fee

        return discounted_fee

