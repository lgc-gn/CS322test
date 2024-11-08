
import pytest
from bank import Account

def test_initial_balance():
    """ 
    Test that given a balance in the arugment of the account constructor, the account stores 
    the inital balance. When no balance is given, the balance should be set to 0 
    """
    account = Account("josiah")
    assert account.get_balance() == 0
    account = Account("josiah", 5)
    assert account.get_balance() == 5
    account = Account("josiah", 3.2)
    assert account.get_balance() == 3.2


def test_deposit():
    """
    Test the account deposit. The input deposit number should add to the balance. A negative 
    number should throw a value error 

    """
    account = Account("josiah")
    account.deposit(30)
    assert account.get_balance() == 30
    account.deposit(2)
    assert account.get_balance() == 32
    
    error_message = 'Deposit amount must be positive'
    with pytest.raises(ValueError, match=error_message):
        account.deposit(-1)
        account.deposit(0)

def test_withdraw():
    """
    Test that withdraw reduces the balance. If it is a negative number or the withdraw amount is greater 
    than the balance, it should throw value errors with diffrent messages 
    """
    account = Account("josiah", 100)
    account.withdraw(30)
    assert account.get_balance() == 70
    
    account = Account("josiah", 0)
    negative_num_error = "Withdrawal amount must be positive"
    with pytest.raises(ValueError, match=negative_num_error): 
        account.withdraw(-5)

    insufficiant_error = "Insufficient funds"
    with pytest.raises(ValueError, match=insufficiant_error): 
        account.withdraw(10)

    


