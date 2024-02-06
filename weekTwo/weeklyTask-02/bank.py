# prompt the user and read in two money amounts
# author name: Andre Machado
# print in human readable format with euro sign and decimal

print("$ python bank.py ")

amount1 = int( input("Enter the amount1(in cent): "))
amount2 = int( input("Enter the amount2(in cent): "))

result = (amount1 / 100 + amount2 / 100)


print(f"The sum of these is: \N{euro sign}{result}")