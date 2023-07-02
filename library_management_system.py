class Register:
    """
    This class will Register User
    """

    def __init__(self, name, mobile_number, email, address, password):
        self.__name = name
        self.__mobile_number = mobile_number
        self.__email = email
        self.__address = address
        self.__password = password

    def get_name(self):
        return self.__name

    def get_mobile_number(self):
        return self.__mobile_number

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_address(self):
        return f"({self.__address.get_post_office()}, {self.__address.get_pin()}, " \
               f"{self.__address.get_city()}, {self.__address.get_state()})"

    def show_profile(self):
        return f"({self.__name}, {self.get_mobile_number()}, {self.get_email()}, " \
               f"({self.__address.get_city()}, {self.__address.get_pin()}, {self.__address.get_city()}, " \
               f"{self.__address.get_state()}))"

    def edit_profile(self, new_name, new_mobile_number, new_email, new_post_office, new_city, new_pin, new_state):
        self.__name = new_name
        self.__mobile_number = new_mobile_number
        self.__email = new_email
        self.__address.edit_address(new_post_office, new_city, new_pin, new_state)


class Login:
    """
    This Class will Validate
    """

    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_user_name(self):
        return self.__username

    def get_user_password(self):
        return self.__password

    def get_username_password(self):
        return f"({self.get_user_name()}, {self.get_user_password()})"

    def login(self, username, password):
        if self.__username == username and self.__password == password:
            print("Login Successfully")
        else:
            print("Invalid Username Or Password")


class Address:
    """
    This Class will Take User Address
    """

    def __init__(self, post_office, pin, city, state):
        self.__post_office = post_office
        self.__pin = pin
        self.__city = city
        self.__state = state

    def get_post_office(self):
        return self.__post_office

    def get_pin(self):
        return self.__pin

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def edit_address(self, new_post_office, new_city, new_pin, new_state):
        self.__city = new_city
        self.__pin = new_pin
        self.__state = new_state
        self.__post_office = new_post_office


class User(Login, Register):
    """
    This Class will User Login and Register to for Library
    """
    pass


class Books:
    """
    This Class contain all books information
    """

    def __init__(self, book_id, book_name, author_name, quantity):
        self.__book_id = book_id
        self.__book_name = book_name
        self.__author_name = author_name
        self.__quantity = quantity

    def get_book_id(self):
        return self.__book_id

    def get_book_name(self):
        return self.__book_name

    def get_author_name(self):
        return self.__author_name

    def get_quantity(self):
        return self.__quantity

    def show_books(self):
        return f"({self.__book_id}, {self.__book_name}, {self.__author_name}, {self.__quantity})"


class Rent:
    """
    This class will give books to user as rent
    """

    def __init__(self, book_id, user_name, quantity):
        self.__book_id = book_id
        self.__name = user_name
        self.__quantity = quantity

    def get_rented_book_id(self):
        return self.__book_id

    def get_rented_user_name(self):
        return self.__name

    def get_rented_quantity(self):
        return self.__quantity

    def show_rented_detail(self):
        return f"({self.__book_id}, {self.__name}, {self.__quantity})"


class Return:
    """
    This class will return back the books from user
    """

    def __init__(self, book_id, user_name, quantity):
        self.__book_id = book_id
        self.__name = user_name
        self.__quantity = quantity

    def get_returned_book_id(self):
        return self.__book_id

    def get_returned_user_name(self):
        return self.__name

    def get_returned_quantity(self):
        return self.__quantity

    def show_returned_detail(self):
        return f"({self.__book_id}, {self.__name}, {self.__quantity})"


class LibraryManagementSystem:
    """
    This Is the Library Class that can do all complex Functions Collaboration
    """

    def __init__(self):
        self.__books = []
        self.__user = []

    def add_books(self, books, users):
        self.__books.append(books.get_book_id())
        self.__user.append(users.get_name())

    def get_books(self):
        return self.__books

    def get_users(self):
        return self.__user

    def show_info(self):
        return f"{self.get_users()}, {self.get_books()}"


if __name__ == '__main__':
    address1 = Address(505, 587965, 'Ranchi', 'Jharkhand')
    user = Register('Saif', '4859756322', 'saif44@gmail.com', address1, '1234')
    book1 = Books(101, 'Titanic', 'James', 5)

    login = Login(user.get_name(), user.get_password())

    # print(user.show_profile())
    # print(login.get_username_password())

    lms = LibraryManagementSystem()
    lms.add_books((), user)

    print(lms.show_info())
# -----------------------------------------------------Test Run------------------------------------------------------
# addr1 = Address(505, 569880, 'Ranchi', 'Jharkhand')
# user1 = Register('Saif', '5897856325', 'saif44@gmail.com', addr1, '1234')
# l1 = Login(user1.get_name(), user1.get_password())
#
# user2 = Register('Kaif', '4875698756', 'kaif16@gmail.com', addr1, '5555')
# l2 = Login(user2.get_name(), user2.get_password())
#
# Login.login(l1, 'Saif', '1234')
#
# print(user1.show_profile())
# print(user2.show_profile())
#
# b1 = Books(101, 'Ghost Rider', 'James', 5)
# b2 = Books(102, 'Titanic', 'Joseph', 10)
#
# print(b1.show_books())
# print(b2.show_books())
#
# r1 = Rent(b1.get_book_id(), user1.get_name(), (b1.get_quantity()) - (b1.get_quantity() - 2))
# r2 = Rent(b2.get_book_id(), user2.get_name(), (b2.get_quantity()) - (b2.get_quantity() - 3))
# re1 = Return(r1.get_rented_book_id(), r1.get_rented_user_name(), r1.get_rented_quantity())
# re2 = Return(r2.get_rented_book_id(), r2.get_rented_user_name(), r2.get_rented_quantity())
#
# print(r1.show_rented_detail())
# print(r2.show_rented_detail())
#
# print(re1.show_returned_detail())
# print(re2.show_returned_detail())


# --------------------------------------------------------Function Test------------------------------------------------
