from bank_account import BankAccount

account = BankAccount()

account.deposit(500)
account.withdraw(200)

print(account.get_balance())
