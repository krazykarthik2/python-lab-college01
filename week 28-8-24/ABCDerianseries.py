# abcderian series python program
str1,str2 = (input("Enter the strings:"),input(""))

out=""
for i1 in str1:
    out+=i1+str2+' '
out = out[:-1]

print(out)