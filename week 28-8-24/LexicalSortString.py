# lexical sort string
str = input("Enter the string:")
l = list(str)
print(l)
l.sort(key=lambda x: ord(x))
new = "".join(l)
print("lexical sorted string:",new)
