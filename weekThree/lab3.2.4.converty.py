'''take an input of an amount of dollars and returns that
absolute amount in cent.'''
# Author: Andre Machado

number = float(input("Please enter an amount: "))
result = int(abs(number * 100))

print('That amount in cent is: \N{euro sign}{}'.format(result))