# puts 10 random numbers into a list, the
# program should then output all the values in the queue, then take the
# numbers from the queue one at a time, print it and the current numbers still
# in the queue.
# Author: Andre Machado

import random

randomlist = random.sample(range(0,100),10)
print(f'Queue is: {randomlist}')
for i in range(0, 10):
    current_number = randomlist.pop(0)
    print(f'current number is {current_number} and the Queue is {randomlist}' )
    
print("the Queue is now empty")
