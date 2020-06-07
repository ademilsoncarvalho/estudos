class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        if self.__is_positive_balance(value):
            self.__balance -= value
        else:
            print("balance is negative")

    def __is_positive_balance(self, value):
        return bool(self.__balance >= value)

    def print_balance(self):
        print('balance is {}'.format(self.__balance))


if __name__ == '__main__':
    bank_account = BankAccount(10)
    bank_account.deposit(15)
    bank_account.print_balance()
    bank_account.withdraw(20)
    print(bank_account)
