# python program to convert celsius to farenheit and viceversa

celsius = float(input("Enter the celsius value:"))
farenheit = celsius * (9 / 5) + 32
print("{0} degree Celsius is {1} degree Farenheit".format(celsius,farenheit))

farenheit = float(input("Enter the farenheit value:"))
celsius = (farenheit - 32) * 5 / 9
print("{0} degree Farenheit is {1} degree Celsius".format(farenheit,celsius))
