class Account:
    def __init__(self, account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} has deposited successfully. New balance is  {self.balance}")
        else:
            print("Amount should bee greater than Zero")
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully. New balance is  {self.balance}")

    def __str__(self):
        return f"Account holder: {self.account_holder}\nbalance: {self.balance}"


class SavingsAccount(Account):
    def __init__(self,account_holder,balance,interest_rate):
            super().__init__(account_holder,balance)
            self.interest_rate = interest_rate

    def add_interest(self):
            interest =self.balance * self.interest_rate/100
            self.balance += interest
            print(f"Interest amount added successfully.New balance is{self.balance}")

    def __str__(self):
           return (f"Savings Account holder:"
                   f" {self.account_holder}\nBalance: {self.balance},"
                   f" Interest rate: {self.interest_rate}")

account = Account('John',10000)
account.withdraw(500)
account.deposit(10000)
print(account)

savings=SavingsAccount('John',10000,14)
savings.deposit(500)
savings.withdraw(200)
print(savings)







