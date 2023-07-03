import random


class Register:
    __account_no = random.randrange(100000000000, 900000000000)

    def __init__(self, name: str, age: int, gender: str, mobile_no: str, email: str, address: vars()) -> None:
        if age <= 0 or age > 100:
            raise ValueError('Invalid Age (1-100)')
        if gender != 'Male' and gender != 'Female':
            raise ValueError('Invalid Gender (Male or Female)')
        if len(mobile_no) != 10:
            raise IndexError('Mobile Cannot Be Less or Greater Than 10')
        if not mobile_no.isnumeric():
            raise ValueError('Invalid Phone Number')
        self.__account_no = Register.__account_no
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__mobile_no = mobile_no
        self.__email = email
        self.__address = address

    def get_account_no(self):
        return self.__account_no

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_mobile_no(self):
        return self.__mobile_no

    def get_email(self):
        return self.__email

    def get_address(self):
        return self.__address


class Address:

    def __init__(self, street: str, post_office: str, pin: str, city: str, state: str) -> None:
        if not post_office.isalpha():
            raise ValueError('Invalid Post Office')
        if not pin.isnumeric():
            raise ValueError('Invalid Pin')
        if len(pin) != 6:
            raise IndexError('Pin Cannot Be Less or Greater Than 6')
        self.__street = street
        self.__post_office = post_office
        self.__pin = pin
        self.__city = city
        self.__state = state


add1 = Address('Los-angle', 'Chasuble', '598756', 'Ranchi', 'Jharkhand')
register = Register('saif', 25, 'Male', '7895465423', 'saif44gmail.com', add1)

print(register.get_address())
