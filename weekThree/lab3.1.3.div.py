
# author name: Andre Machado
# program that reads in two numbers and
# outputs the integer answer and remainder

x = int(input("Enter first number: "))
y = int(input("Enter the number you want divide by: "))
answer = int(x // y)
remainder = x % y

print("{} divided by {} is {} with remainder {}" .format(x, y, answer, remainder))
