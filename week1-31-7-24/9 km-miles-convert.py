#python program to convert km to miles
km = float(input("Enter value in kilometers: "))
conv_fac = 0.621371
miles = km * conv_fac
print('%0.2f kilometers is equal to %0.2f miles'%(km,miles))
# and viceversa
miles = float(input("Enter value in miles: "))
conv_fac = 1.60934
km = miles * conv_fac
print('%0.2f miles is equal to %0.2f kilometers'%(miles,km))
