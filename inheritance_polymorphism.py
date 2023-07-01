# Aggregation (Has a relationship)--------------------------------------------------------------------------
# In Aggregation cannot get private attribute But you can make a function to get the private attribute

class Customer:

    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def get_address(self):
        return f"({self.address.get_city()}, {self.address.pin}, {self.address.state})"

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.edit_address(new_city, new_pin, new_state)


class Address:

    def __init__(self, city, pin, state):
        self.__city = city
        self.pin = pin
        self.state = state

    def get_city(self):
        return self.__city

    def edit_address(self, new_city, new_pin, new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state


add1 = Address('Ranchi', 568996, 'Jharkhand')
cust1 = Customer('Saif', 'Male', add1)

# print(cust1.get_address())

cust1.edit_profile('Kaif', 'Goa', 155896, 'Mumbai')


# print(cust1.get_address())

# Inheritance----------------------------------------------------------------------


class Phone:

    def __init__(self, price: int, brand: str, camera: int):
        self.price = price
        self.brand = brand
        self.camera = camera


class SmartPhone(Phone):
    pass


s = SmartPhone(2000, "Nokia", 13)
