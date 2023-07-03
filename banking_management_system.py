class Register:
    __account_no = 1005687456982548

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

        Register.__account_no += 1

    def get_account_no(self):
        return self.__account_no

    def get_name(self):
        return self.__name

    def set_name(self, new_name: str) -> None:
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age: int) -> None:
        if new_age <= 0 or new_age > 100:
            raise ValueError('Invalid Age (1-100)')
        self.__age = new_age

    def get_gender(self):
        return self.__gender

    def set_gender(self, new_gender: str) -> None:
        if new_gender != 'Male' and new_gender != 'Female':
            raise ValueError('Invalid Gender (Male or Female)')
        self.__gender = new_gender

    def get_mobile_no(self):
        return self.__mobile_no

    def set_mobile_no(self, new_mobile_no: str) -> None:
        if len(new_mobile_no) != 10:
            raise IndexError('Mobile Cannot Be Less or Greater Than 10')
        if not new_mobile_no.isnumeric():
            raise ValueError('Invalid Phone Number')
        self.__mobile_no = new_mobile_no

    def get_email(self):
        return self.__email

    def set_email(self, new_email: str) -> None:
        self.__email = new_email

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

    def __repr__(self):
        return f"({self.__street}, {self.__post_office}, {self.__pin}, {self.__city}, {self.__state})"


class User(Register):

    def __init__(self, name: str, age: int, gender: str, mobile_no: str, email: str, address: vars(),
                 password: str) -> None:
        super().__init__(name, age, gender, mobile_no, email, address)
        self.__password = password

    def get_password(self):
        return self.__password


class Bank(User):

    def __init__(self, name: str, age: int, gender: str, mobile_no: str, email: str, address: vars(), password: str):
        super().__init__(name, age, gender, mobile_no, email, address, password)
        self.__account_balance = 0

    def get_balance(self):
        return self.__account_balance

    def set_balance(self, amount: int or float) -> None:
        if type(amount) != int and float:
            raise ValueError('Invalid Amount')
        if amount < 0:
            raise ValueError('Amount Must Be Positive')
        self.__account_balance = amount

    def deposit(self, amount: int or float) -> None:
        if type(amount) != int and float:
            raise ValueError('Invalid Amount')
        if amount < 0:
            raise ValueError('Amount Must Be Positive')
        self.__account_balance += amount

    def withdraw(self, amount: int or float) -> None:
        if type(amount) != int and float:
            raise ValueError('Invalid Amount')
        if amount < 0:
            raise ValueError('Amount Must Be Positive')
        self.__account_balance -= amount

    def transfer(self, amount, other: int or float) -> None:
        if type(amount) != int and float:
            raise ValueError('Invalid Amount')
        if amount < 0:
            raise ValueError('Amount Must Be Positive')
        self.__account_balance -= amount
        other.__account_balance += amount


if __name__ == '__main__':
    try:
        add1 = Address('Los-angle', 'Chasuble', '598756', 'Ranchi', 'Jharkhand')
        user1 = Bank('saif', 25, 'Male', '7895465423', 'saif44gmail.com', add1, '1234')
        user2 = Bank('kaif', 25, 'Male', '5879865456', 'kaif55@gmail.com', add1, '5566')
        user1.set_balance(500)
        user1.deposit(200)
        user1.withdraw(100)
        user1.set_age(26)
        user1.transfer(200, user2)
    except Exception as error:
        print(error)
    else:
        print(user1.get_balance())
        print(user2.get_balance())
        print(user1.get_age())
        print(user1.get_account_no())
        print(user2.get_account_no())
