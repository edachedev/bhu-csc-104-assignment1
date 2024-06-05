class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        print("Withdrawal method must be implemented by subclass")

    def __str__(self):
        return f"Account Number: {self.__account_number}, Account Holder: {self.__account_holder}, Balance: {self.__balance}"
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0):
        super().__init__(account_number, account_holder, balance)
        self.__interest_rate = 0.005

    def deposit(self, amount):
        super().deposit(amount)
        interest = amount * self.__interest_rate
        super().deposit(interest)
        return super().get_balance()

    def withdraw(self, amount):
        if amount <= 700000:
            super().withdraw(amount)
            return super().get_balance()
        else:
            print("Withdrawal amount exceeds limit")


class CurrentAccount(Account):
     def __init__(self, account_number, account_holder, balance=0):
          super().__init__(account_number, account_holder, balance)

     def withdraw(self, amount):
          super().withdraw(amount)
          return super().get_balanced()



savings_account = SavingsAccount("SAV123", "John Doe", 10000)
print(savings_account)
savings_account.deposit(5000)
print(savings_account)
savings_account.withdraw(30000)
print(savings_account)

current_account = CurrentAccount("CUR456", "Jane Doe", 20000)
print(current_account)
current_account.deposit(10000)
print(current_account)
current_account.withdraw(15000)
print(current_account)

