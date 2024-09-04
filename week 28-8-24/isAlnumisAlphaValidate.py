# validate username and PANCard Number
#use isalpha() function
# use isalnum() function 

username = input("Enter username(NO SPECIAL CHAR): ")
pancard = input("Enter PANCard Number:(ALL CAPS) ")

if username.isalpha():pass
else:
    print("Username is invalid")
    exit(0)

if pancard.isalnum() and len(pancard) == 10 and pancard.isupper():pass
else:
    print("PANCard Number is invalid")
    exit(0)

print("Username:", username)
print("PANCard Number:", pancard)
