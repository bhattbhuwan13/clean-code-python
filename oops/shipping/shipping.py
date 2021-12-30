# Class attributes are those attributes that are shared among all instances of the class.
# They are not specific to any one object.

# Note: The class doesn't have any scope and hence doesn't appear in LEGB
class ShippingContainer:

    next_serial = 1337

    # Static methods are used to group code that are related to a class rather than a specific object

    @staticmethod
    def _generate_serial(): # No self argument required for the static method, we are dealing with class variable and not instance variable
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()

