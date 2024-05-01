# A function to be tested

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


# only catch an exception if you are doing something with it


#The way to run a program only if using its own
if __name__ == "__main__":
    #checking calculation using assert
    assert withdraw(20) == 80, "incorret calculation"
    try:
        withdraw(-1)
        assert False, "shoud have thrown a value error"
    except ValueError as ve:
        pass
    try:
        withdraw(110)
        assert False, "Cant withdraw more than in its value"
    except ValueError as ve:
        pass
    print("all good")