from account import BankAccount

if __name__ == '__main__':
    account = BankAccount("12345", 500)
    print(account.check_balace())
    account.deposit(140)
    print(account.check_balace())
    account.withdraw(200)
    print(account.check_balace())
    account.withdraw(400) # error
    print(account.check_balace())