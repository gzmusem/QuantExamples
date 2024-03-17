#类的私有变量示例

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # 私有变量
        self.__balance = balance                # 私有变量
        
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance.")
            
account = BankAccount("1234567890", 1000)
# account.__balance = 2000  # 这行代码会引发AttributeError,因为__balance是私有变量
account.deposit(500)
account.withdraw(200)