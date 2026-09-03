# Wrapping data and functions into a single unit (object) is known as encapsulation. 
# In Python, we can achieve encapsulation by using private attributes and methods.

# Create Account class with 2 attributes - balance and account no. Craete methods for debit, credit, and printing the balance.

class Account:
    
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Debited {amount}. New balance is {self.balance}")

    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount}. New balance is {self.balance}")

    def get_balance(self):
        return self.balance


account1 = Account("123456", 1000)
account1.debit(500)
account1.credit(200)


