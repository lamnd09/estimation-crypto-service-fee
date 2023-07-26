class Transaction:
    def __init__(self, from_amount, from_network, from_asset, to_network, to_asset, fee_asset):
        self.from_amount = from_amount
        self.from_network = from_network
        self.from_asset = from_asset
        self.to_network = to_network
        self.to_asset = to_asset
        self.fee_asset = fee_asset
