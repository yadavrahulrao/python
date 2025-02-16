class BankAccount:
  def __init__(self,acc_no ,name,date_of_open , balance ):
    self.acc_no = acc_no
    self.date_of_open = date_of_open
    self.balance = balance
    self.name = name

  def deposite(self,amount):
    self.balance += amount
    print("Deposited:",amount,"Balance:",self.balance)

  def debit(self,amount):
    if amount <= self.balance :
      self.balance -= amount
      print("Debited:",amount,"Balnce:",self.balance)
    else :
      print("not sufficient balance")

  def CheckBalance(self):
    print("Balance:",self.balance)

bank = BankAccount(1001003067,"Rahul","01-03-2004",9000)

bank.CheckBalance()

bank.deposite(25000)

bank.debit(4000)

bank.CheckBalance()



