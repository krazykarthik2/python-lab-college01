BRICS=['brazil','russia','india','china','srilanka']
country = input("Enter a country name:")
if country.replace(" ","").lower() in BRICS:
    print("Country is a part of BRICS")
else:
    print("Country is not a part of BRICS")
