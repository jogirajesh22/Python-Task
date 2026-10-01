import random
class Customeraccount:
    def __init__(self,name,email,Phone_number,Age):
        self.__name=name
        self.__email=email
        self.__Phone_number=Phone_number
        self.__Age=Age
        self.__email_verified = False
        self.__phone_verified = False

        self.__emailotp=None
        self.__phoneotp=None
        self.validate_customer()
        self.__balance=0
        print("name:",self.__name)
        print("email:",self.__email)
        print("phone number:", self.__Phone_number)
        print("Age:", self.__Age)
    def update(self,email,phone_number):
        self.__email=email
        self.__phone_number=phone_number

    def sendemailotp(self):
        self.__emailotp=random.randint(1000,9999)
        print("email otp generate:",self.__emailotp)


    def verifyEmailOTP(self,otp):
        if otp==self.__emailotp:
            self.__email_verified=True
            print("Email verfication successful")
        else :
           print("Invalid email otp")

    def sendphoneotp(self):
        self.__phoneotp=random.randint(1000,9999)
        print("phone otp generate:",self.__phoneotp)
    
     
    def verifyphoneOTP(self,otp):
        if otp==self.__phoneotp:
            self.__phone_verified=True
            print("phone otp verfication successful")
        else :
            print("Invalid phone otp")

    def validate_customer(self):

        if self.__name == "":
            print("Name cannot be empty")

        if "@" not in self.__email or "." not in self.__email:
            print("Invalid email address")

        if self.__Phone_number == "":
            print("Phone number cannot be empty")

        if self.__Age <= 0:
            print("Age must be greater than zero") 

    def isfullyverified(self):
         if self.__email_verified and self.__phone_verified:
             return      True
         else:
             return     False        

    def deposit(self,amount):
        if amount  <=0:
            print("Deposit amount must be greater than zero")
            return

        self.__balance = self.__balance + amount

        print("Amount deposited:", amount)
        print("Current balance:", self.__balance)

    def  withdraw(self,amount):
        if amount <= 0:
               print("Withdrawal amount must be greater than zero")
               return

        if amount > self.__balance:
              print("Insufficient balance")
              return

        self.__balance = self.__balance - amount

        print("Amount withdrawn:", amount)
        print("Current balance:", self.__balance)
    def getbalance(self):
        return self.__balance

Customer=Customeraccount("rajesh","rajesh@email.com","9963558900",23) 
print("Customer created successfully")

Customer.update("raju@gmail.com","9963445698")

Customer.sendemailotp()

emailotp=Customer._Customeraccount__emailotp
Customer.verifyEmailOTP(emailotp)

Customer.sendphoneotp()

phoneotp=Customer._Customeraccount__phoneotp
Customer.verifyphoneOTP(phoneotp)

Customer.isfullyverified()

Customer.deposit(5000)

Customer.withdraw(2000)

print("balance:",Customer.getbalance())

#test case1

Customer=Customeraccount("rajesh","test","90000000",23)

#test case2
Customer=Customeraccount("rajesh","rajesh@email.com","9963558900",23) 
Customer.sendemailotp()
Customer.verifyEmailOTP(1111)

#test case3
Customer.deposit(-100)

#test case4
Customer.deposit(3000)

#test case5
Customer.withdraw(4000)