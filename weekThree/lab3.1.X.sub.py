# program to subtract on number from another
# author name: Andre Machado
# input reads in a string so we need to convert it into an int
# so we can perform mathematical operations

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
result = x - y

print(f"{x} minus {y} is {x - y}")
print("Using format()")
print("{} minus {} is {} " .format(x, y, result))