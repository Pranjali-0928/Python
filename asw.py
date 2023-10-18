# import random
# for i in range(4, 15):
#  y = random.randrange(9)
#  print(y)
 
 
import string
import random

# Randomly choose a letter from all the ascii_letters
randomLetter = random.choice(string.ascii_letters)
for i in range(1, 21):
 y = random.randrange(9)
print(str(y)+randomLetter)