# This is a coin toss game
import random

count =0



for guessesTaken in range(100):
    
    number = random.randint(1, 2)

    if number == 1:
    
        print ('tails')
    else:
        print  ('heads')
        count = count + 1

print ('heads: ' + str(count))
    
