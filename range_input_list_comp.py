start,end = (int(input("Enter start of range:")),int(input("Enter end of range:")))
l = [i for i in range(start,end+1)]
l.reverse()
print("final output:",end="")
print(l)