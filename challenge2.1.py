class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited ₹{}. Current balance : ₹{}\n".format(
          amount, self.__account_balance))
    else:
      print("Invalid deposit amount. Please deposit a positive amount.\n")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdraw ₹{}. Current balance: ₹{}\n".format(
          amount, self.__account_balance))
    else:
      print("Invalid withdrawl amount of insufficient balance.\n")

  def display_balance(self):
    print("Account balance for {} (Account #{}): ₹{}.\n".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))


account = BankAccount(account_number="123456789",
                      account_holder_name="Barani dharan",
                      initial_balance=9000.0)

account.display_balance()
account.deposit(50000.0)
account.withdraw(3000.0)
account.display_balance()
