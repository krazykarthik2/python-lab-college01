import sum
import mul 

print("1.Sum\n2.Multiplication")
choice = int(input("Enter your choice:"))
if choice in [1,2]:
    a,b =  int(input("enter 1st number:")),int(input("enter 2nd number:"))
    if choice == 1:
        print(sum.summation(a,b))
    elif choice == 2:
        print(mul.multiplication(a,b))
        
else:
    print("invalid choice")

