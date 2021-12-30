# Class attributes are those attributes that are shared among all instances of the class.
# They are not specific to any one object.

# Note: The class doesn't have any scope and hence doesn't appear in LEGB
class ShippingContainer:

    next_serial = 1337

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1

