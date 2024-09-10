from decimal import Decimal
class Account:


    def __init__(self, name: str, pin: str, balance: Decimal = 0.00):
        self.name = name.upper()
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        if amount < Decimal(0.00):
            raise ValueError("Amount cannot be less than zero")
        self.balance += amount


account1 = Account("david", "1234")
account2 = Account("daniel", "0000")

account2.deposit(1000000)
print(account2.balance)


