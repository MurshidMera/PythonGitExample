class BankAccount:

    def __init__(self, name, accno, balance):
        self.name = name
        self.accno = accno
        self.balance = balance

    def __del__(self):
        print("Account is closed.")

    def show_details(self):
        print("Name :",self.name)
        print("Account No :",self.accno)
        print("Balance :", self.balance)

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} deposited succssfully ")

    def getBalance(self):
        return self.balance 


abash_acc = BankAccount("Abhash", 123412415324, 20000)

sharath_acc = BankAccount("Sharath", 4121313123, 50000)

#print(vars(abash_acc)) #Printing complete object value
#print(sharath_acc.__dict__) #double underscore obj.__dict__, print complete object value.
print(sharath_acc.show_details())
sharath_acc.deposit(5000)
print("Current Blance ",sharath_acc.getBalance())

del abash_acc