import random
n_num = [random.randint(0,100) for i in range(0,10+1)]
even = [i for i in n_num if i%2==0]
odd = [ i for i in n_num if i%2==1]
print('odd list:',end="")
print(odd)
print('odd list:',end="")
print(even)
