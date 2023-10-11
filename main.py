import random
from validate import validate_pan, validate_aadhaar

IFSCDict = {'ICICI': 'ICICI163805', 'IOB': 'IOBA109867', 'SBI': 'SBIA234690'}
bankDict = {}
accntDict = []


class BankAccount:

  def __init__(self, bankName, IFSC, accntNumber, name, age, gender, DOB,
               address, city, accntType, balance, PAN, Aadhaar):
    self.bankName = bankName
    self.IFSC = IFSC
    self.accntNumber = accntNumber
    self.name = name
    self.age = age
    self.gender = gender
    self.DOB = DOB
    self.address = address
    self.city = city
    self.accountType = accntType
    self.balance = balance
    self.PAN = PAN
    self.Aadhaar = Aadhaar

    if self.bankName in bankDict:
      bankDict[self.bankName].append(self.name)
    else:
      bankDict[self.bankName] = [self.name]

  def createAccount(self):
    print('Account Created Successfully.')

  @classmethod
  def deleteAccount(self, accntNumber):
    for i in accntDict:
      if (i.accntNumber == accntNumber):
        bankDict[bankName].remove(i)
        print('Account Deleted Successfully.')
        break

  @classmethod
  def updateName(self, accntNumber, newName):
    for i in accntDict:
      if (i.accntNumber == accntNumber):
        i.name = newName
        print('Account Updated Successfully.')
        break

  @classmethod
  def updateAddress(self, accntNumber, newAddress):
    for i in accntDict:
      if (i.accntNumber == accntNumber):
        i.address = newAddress
        print('Account Updated Successfully.')
        break

  @classmethod
  def updateDOB(self, accntNumber, newDOB):
    for i in accntDict:
      if (i.accntNumber == accntNumber):
        i.DOB = newDOB
        print('Account Updated Successfully.')
        break

  @classmethod
  def deposit(self, accntNumber, amnt):
    for i in accntDict:
      if (i.accntNumber == accntNumber):
        i.balance = str(int(i.balance) + amnt)
        print('Amount Deposited Successfully.')
        break

  @classmethod
  def withdraw(self, accntNumber, amnt):
    for i in accntDict:

      if (i.accntNumber == accntNumber):
        if (int(i.balance) < amnt):
          print('Insufficient Balance.')
          break
        else:
          i.balance = str(int(i.balance) - amnt)
          print('Amount Withdrawn Successfully.')
          break

  @classmethod
  def transfer(self, accntNumber, amnt, accntNumber2):
    BankAccount.withdraw(accntNumber, amnt)
    BankAccount.deposit(accntNumber2, amnt)

  @classmethod
  def balance(self, accntNumber):
    for i in accntDict:
      if (i.accntNumber == accntNumber):
        print('Balance', " = ", i.balance)
        break


def randomnumber(N):
  minimum = pow(10, N - 1)
  maximum = pow(10, N) - 1
  return random.randint(minimum, maximum)


while (True):
  print("")
  print("1: Press 1 to create an account")
  print("2: Press 2 to delete an account")
  print("3: Press 3 to update account")
  print("4: Press 4 to deposit")
  print("5: Press 5 to withdraw")
  print("6: Press 6 to transfer funds")
  print("7: Press 7 to search")
  print("8: Press 8 to check balance")

  choice = int(input("Enter your choice: "))

  for i in accntDict:
    print(i.accntNumber, ' : ', i.name)

  if choice == 1:
    bankName = input("Enter the Bank Name: ")
    IFSC = IFSCDict[bankName]
    name = input("Enter Account Holder Name: ")
    age = input("Enter the age: ")
    gender = input("Enter the gender: ")
    DOB = input("Enter the DOB: ")
    address = input("Enter the address: ")
    city = input("Enter the city: ")
    accntType = input("Enter the account type: ")
    balance = input("Enter the balance: ")
    while (True):
      PAN = input("Enter the PAN: ")
      if (validate_pan(PAN)):
        break
      else:
        print("Invalid PAN, Enter again")
    while (True):
      Aadhaar = input("Enter the Aadhaar Number: ")
      if (validate_aadhaar):
        break
      else:
        print("Invalid Aadhaar Number, Enter again")
    accntNumber = IFSCDict[bankName][7:] + str(randomnumber(12))
    obj = BankAccount(bankName, IFSC, accntNumber, name, age, gender, DOB,
                      address, city, accntType, balance, PAN, Aadhaar)
    obj.createAccount()
    accntDict.append(obj)
  elif choice == 2:
    bankName = input("Enter the Bank Name: ")
    name = input("Enter the account holder name: ")
    BankAccount.deleteAccount(name)
  elif choice == 3:
    print("Press A to update name")
    print("Press B to update address")
    print("Press C to update DOB")

    ch = input("Enter to update details: ")
    bankName = input("Enter bank name: ")
    accntNumber = input("Enter account number: ")
    if ch == 'A':
      name = input("Enter the new name: ")
      BankAccount.updateName(accntNumber, name)
    elif ch == 'B':
      address = input("Enter the new address: ")
      BankAccount.updateAddress(accntNumber, address)
    elif ch == 'C':
      DOB = input("Enter the new DOB: ")
      BankAccount.updateDOB(accntNumber, DOB)
  elif choice == 4:

    accntNumber = input('Enter the account number: ')
    amount = int(input('Enter the amount to deposit: '))
    BankAccount.deposit(accntNumber, amount)
  elif choice == 5:

    accntNumber = input('Enter the account number: ')
    amount = int(input('Enter the amount to withdraw: '))
    BankAccount.withdraw(accntNumber, amount)

  elif choice == 6:
    bankName = input('Enter the bank nam: ')
    accntNumber = input('Enter the account number: ')
    amount = int(input('Enter the amount to transfer: '))
    bankName2 = input('Enter the bank nam: ')
    accntNumber2 = input('Enter the account number: ')
    BankAccount.transfer(accntNumber, amount, accntNumber2)

  elif choice == 7:
    print("Press A to search by account number")
    print("Press B to search by name")
    print("Press C to search by type of account")

    ch = input("Enter your choice: ")
    if ch == 'A':
      p = input("Enter your account number")
      for i in accntDict:
        if (i.accntNumber == p):
          print(i.name, " ", i.accntNumber, " ", i.address, " ", i.balance)

    elif ch == 'B':
      p = input("Enter your name")
      for i in accntDict:
        if (i.name == p):
          print(i.name, " ", i.accntNumber, " ", i.address, " ", i.balance)
    elif ch == 'C':
      p = input("Enter your type of account")
      for i in accntDict:
        if (i.accntType == p):
          print(i.name, " ", i.accntNumber, " ", i.address, " ", i.balance)
    else:
      print("Invalid Choice!!")

  elif choice == 8:
    accntNumber = input("Enter the account number: ")
    bankName = input("Enter Bank name: ")
    BankAccount.balance(accntNumber)
  else:
    print("Please enter a valid choice")
