# Wrapping data and functions into a single unit (object) is known as encapsulation. 
# In Python, we can achieve encapsulation by using private attributes and methods.

# Create Account class with 2 attributes - balance and account no. Craete methods for debit, credit, and printing the balance.

# class Account:
    
#     def __init__(self, account_no, balance):
#         self.account_no = account_no
#         self.balance = balance

#     def debit(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#             print(f"Debited {amount}. New balance is {self.balance}")

#     def credit(self, amount):
#         self.balance += amount
#         print(f"Credited {amount}. New balance is {self.balance}")

#     def get_balance(self):
#         return self.balance


# account1 = Account("123456", 1000)
# account1.debit(500)
# account1.credit(200)

# del keyword is used to delete an object in Python. When we delete an object, the memory occupied by that object is released back to the system.

# del account1.account_no

# print(account1.account_no) # This will raise an AttributeError because the account_no attribute has been deleted from the account1 object.

# private (attributes or methods) are meant to be used only within class and are not accessible from outside the class. 
# In Python, we can make an attribute or method private by prefixing it with double underscores (__).


class Account:
    def __init__(self,account_no,account_pass):
        self.account_no = account_no
        self.__account_pass = account_pass

    def get_account_pass(self):
        return self.__account_pass

    def __get_account_password(self):
        return self.__account_pass

account1 = Account("123456", "password123")

# This will print the account number
print(account1.account_no)

# This will raise an AttributeError because the __account_pass attribute is private and cannot be accessed from outside the class.
print(account1.__account_pass) 


 # This will print the account password because we are accessing it through a public method defined in the class.
print(account1.get_account_pass())