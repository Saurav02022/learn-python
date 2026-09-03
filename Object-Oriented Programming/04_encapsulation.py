# ENCAPSULATION AND ATTRIBUTE ACCESS

# Definition:
# Encapsulation keeps data and the methods that control it inside a class.
# Public, protected, and private names show the intended level of access.

# Use:
# Use encapsulation so the class can validate and control its data.

class Account:
    def __init__(self, balance):
        self.balance = balance  # Public
        self._account_type = "Savings"  # Protected by convention
        self.__pin = "1234"  # Private by name mangling

    def check_pin(self, pin):
        return self.__pin == pin


account1 = Account(1000)
print(account1.balance)
print(account1._account_type)
print(account1.check_pin("1234"))

# Public data is meant for normal outside use.
# One underscore means internal use by convention.
# Two underscores reduce accidental direct access.
# Python private names are not a security system.
# Expected output:
# 1000
# Savings
# True

# Common mistake:
# Do not store or print real passwords and PINs as plain text.

# Practice:
# Add a deposit() method that accepts only positive amounts.
