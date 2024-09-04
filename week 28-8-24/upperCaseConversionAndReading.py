# convert string to uppercase if it contains at 2 uppercase in first 4 character
s = input("Enter a string: ")
upper = 0
for i in s[:4]:
    if i.isupper():
        upper += 1
if upper>=2:
    s = s.upper()
print(s)