import random

for i in range(100):
    letters = ['a','b','c','d','e']
    print(str(i+1) +'.', random.choice(letters))

