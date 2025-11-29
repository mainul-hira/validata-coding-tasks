class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"A/C No: {self.account_number} - Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self.balance < amount:
            print(f"A/C No: {self.account_number} - Insufficient funds.")
        else:
            self.balance -= amount
            print(f"A/C No: {self.account_number} - Withdrew ${amount}. New balance: ${self.balance}")

    def check_balance(self):
        print(f"A/C No: {self.account_number} - Current balance: ${self.balance}")
        return self.balance

    def display_details(self):
        print(f"Account Details of A/C No: {self.account_number}:")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")

if __name__ == "__main__":
    account = BankAccount("123456789", "Mainul Hoque", 1000)
    account.display_details()
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)
    account.display_details()
