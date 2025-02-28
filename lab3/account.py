class TransactionException(Exception):
    pass

class BankAccount:

    def __init__(self, account_number: str, initial_balance: int):
        self.balance = initial_balance
        self.account_number = account_number
        self.minimal_leftover = 100
    
    def check_balace(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if (self.balance - amount >= self.minimal_leftover):
            self.balance -= amount
        else:
            raise TransactionException(f"After withdraw balance leftover will be under minimal allowed amount of {self.minimal_leftover}. Operation not performed.")
