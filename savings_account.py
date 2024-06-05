
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
            raise ValueError("Withdrawal amount exceeds limit")