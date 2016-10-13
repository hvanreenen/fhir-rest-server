from models.address import Address


class Address(Address):


    def __init__(self, jsondict=None, strict=True):
        super(Address, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return "{}, {}, {}, {}".format(self.line, self.postalCode, self.city, self.country)

    @staticmethod
    def from_str(address):
        a = Address()
        parts = address.split(',')
        if len(parts) == 4:
            a.line = [parts[0]]
            a.postalCode = parts[1]
            a.city = parts[2]
            a.country = parts[3]
        return a


