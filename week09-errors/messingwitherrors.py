# this program is to show how to use try except

#filename = 'data.txt'
import sys

#print out the name of the folder and the argument from the user
print(sys.argv)

try:
   filename = sys.argv[1]
   print(filename)
except IndexError as ie:
   print("Please enter the filename as an argument")
   print(ie)

#Another way
try:
   filename = sys.argv[1]
   print(filename)
   with open(filename) as fp:
      print(fp.read())
except IndexError as ie:
   print("Please enter the filename as an argument")
   print(ie)
except FileNotFoundError:
   print(f"file {filename} not found, please enter a filename that exists")