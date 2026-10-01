class BankAccount():
    def Create_account(self,customer_name,account_number,initial_deposit):
        self.customer_name=customer_name
        self.account_number=account_number
        self.balance=initial_deposit
       
        self.transactions = []

    def deposit(self,amount):
        if amount <=0:
            print("Reject zero or negative amounts")
        else:
            self.balance=self.balance+amount
            self.transactions.append("Deposited: " + str(amount))
            print("deposit successfully")

    def withdraw(self,amount):
        if amount <=0:
            print("Reject zero or negative amounts")
        elif amount > self.balance:
            print(" insufficient")
        else:
            self.balance=self.balance-amount
            self.transactions.append("Withdrawn: " + str(amount))
            print("withdraw sucvessfuly")

    def check_balance(self):
        print("account_name:",self.account_number)
        print("name:",self.customer_name)
        print("balance:",self.balance)

    def transfer_money(self,amount,receiver):
         if amount <=0:
                    print("Reject zero or negative amounts")
         elif amount > self.balance:
                    print(" insufficient")
         else:
                self.balance = self.balance - amount
                receiver.balance = receiver.balance + amount
                print("Transfer successfully")

                self.transactions.append( "Transferred " + str(amount) +  " to account " + str(receiver.account_number))

                receiver.transactions.append("Received " + str(amount) +" from account " + str(self.account_number))
    
    def transaction_history(self):
        print("Transaction History:")

        if len(self.transactions) == 0:
            print("No transactions found")
        else:
             for transaction in self.transactions:
                print(transaction)



accounts={}
name=input("Enter Customer name:",)
account_number=int(input("Enter account number:") )
initial_deposit=int(input("enter initial deposit"))

if initial_deposit<500:
    print("Initial deposit must be at least ₹500")

elif account_number in accounts:
    print("Account number already exists")

else:
     account = BankAccount()
     account.Create_account(name,account_number, initial_deposit)
     
     accounts[account_number] = account
     print("account created succesfully")

account_number=int(input("enter a acc num:"))
amount=int(input("enter a amount:"))
if account_number in accounts:
    accounts[account_number].deposit(amount)

    

 
   
account_number =int(input("Enter account number: "))
amount = int(input("Enter amount: "))

if account_number in accounts:
   accounts[account_number].withdraw(amount)



account_number = int(input("Enter account number: "))


if account_number in accounts:
    accounts[account_number].check_balance()

#Transfer Money

send_account =int(input("Enter a send account:"))   
receive_account=int(input("enter a receive account:"))
amount=float(input("enter a amount"))

if  send_account not in accounts:
    print("Sender account does not exist")

elif receive_account not in accounts:
    print("Receiver account does not exist")

elif send_account == receive_account:
    print("Cannot transfer money to the same account")

else:
     sender = accounts[send_account]
     receiver = accounts[receive_account]

     sender.transfer_money(amount,receiver)



account_number = int(input("Enter account number: "))

if account_number in accounts:
    accounts[account_number].transaction_history()
else:
    print("Account does not exist")