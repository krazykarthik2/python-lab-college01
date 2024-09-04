import powers

print("1.Cube\n2.Square")
choice = int(input("Enter your choice:"))
if choice in [1,2]:
    n = int(input("Enter the number:"))
    if choice == 1:
        print(powers.cube(n))
    elif choice == 2:
        print(powers.square(n))
else:
    print("invalid choice")
