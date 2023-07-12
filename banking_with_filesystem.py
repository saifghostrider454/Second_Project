# TEST CASES FOR BANKING
from jedi.plugins import pytest

from banking_management_system import Bank


def test_deposit_valid_amount(self):
    bank = Bank('John', 25, 'Male', '1234567890', 'john@gmail.com', {'city': 'New York', 'state': 'NY', 'zip': '10001'},
                'password')
    bank.deposit(100)
    assert bank.get_balance() == 100


def test_withdraw_valid_amount(self):
    bank = Bank('John', 25, 'Male', '1234567890', 'john@gmail.com', {'city': 'New York', 'state': 'NY', 'zip': '10001'},
                'password')
    bank.set_balance(100)
    bank.withdraw(50)
    assert bank.get_balance() == 50


def test_transfer_valid_amount(self):
    bank1 = Bank('John', 25, 'Male', '1234567890', 'john@gmail.com',
                 {'city': 'New York', 'state': 'NY', 'zip': '10001'}, 'password')
    bank2 = Bank('Jane', 30, 'Female', '0987654321', 'jane@gmail.com',
                 {'city': 'Los Angeles', 'state': 'CA', 'zip': '90001'}, 'password')
    bank1.set_balance(100)
    bank2.set_balance(50)
    bank1.transfer(50, bank2)
    assert bank1.get_balance() == 50
    assert bank2.get_balance() == 100


def test_deposit_negative_amount(self):
    bank = Bank('John', 25, 'Male', '1234567890', 'john@gmail.com', {'city': 'New York', 'state': 'NY', 'zip': '10001'}, 'password')
    with pytest.raises(ValueError):
        bank.deposit(-100)


def test_withdraw_negative_amount(self):
    bank = Bank('John', 25, 'Male', '1234567890', 'john@gmail.com', {'city': 'New York', 'state': 'NY', 'zip': '10001'}, 'password')
    with pytest.raises(ValueError):
        bank.withdraw(-100)


def test_transfer_negative_amount(self):
    bank1 = Bank('John', 25, 'Male', '1234567890', 'john@gmail.com', {'city': 'New York', 'state': 'NY', 'zip': '10001'}, 'password')
    bank2 = Bank('Jane', 30, 'Female', '0987654321', 'jane@gmail.com', {'city': 'Los Angeles', 'state': 'CA', 'zip': '90001'}, 'password')
    bank1.set_balance(100)
    bank2.set_balance(50)
    with pytest.raises(ValueError):
        bank1.transfer(-50, bank2)
