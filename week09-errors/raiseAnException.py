# Demonstrate raising an exception
# program prompts the user for an amount and withdraws it from account

balance = 100

def withdraw(amount):
    # to be able to reach the balance outside of the def
    global balance
    # handle with user input less than zero
    if amount < 0:
        raise ValueError("amount should always be greater than 0")
    if amount > 100:
        raise ValueError("not enough funds")
    balance = balance - amount
    return balance

amount = int(input("Amount to withdraw: "))

print(withdraw(amount))

# only catch an exception if you are doing something with it

