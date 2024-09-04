# count uppercase, lowercase and digits and space and special characters in given input
str = input("Enter a string: ")
upper = 0
lower = 0
digit = 0
spaces = 0
special = 0

for i in str:
    if i.isalpha():
        if i.isupper():
            upper += 1
        else:
            lower += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        spaces += 1
    else:
        special += 1

print("Uppercase: ", upper)
print("Lowercase: ", lower)
print("Digits: ", digit)
print("Spaces: ", spaces)
print("Special characters: ", special)
