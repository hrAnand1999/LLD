from Address.addressInterface import AddressInterface

class Address(AddressInterface):

    def __init__(self, pincode: int):
        super().__init__()
        self.pincode = pincode

    def getPincode(self) -> int:
        return self.pincode
