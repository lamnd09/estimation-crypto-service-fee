class Provider:
    def __init__(self, name, fee):
        self.name = name
        self.fee = fee

    def to_dict(self):
        return {
            "name": self.name,
            "fee": self.fee
        }
