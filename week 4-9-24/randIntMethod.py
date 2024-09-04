#write a program to generate 10 random numbers between 1 to 100 using randInt() method

import random

arr=[]
for i in range(10):
    arr.append(random.randint(1, 100))
print("Your 10 random numbers are:")
print(",".join(str(x) for x in arr))