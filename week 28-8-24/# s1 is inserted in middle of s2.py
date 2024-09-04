# s1 is inserted in middle of s2
s1,s2 = (input("Enter two strings: ").split())
firsthalf = s1[:len(s1)//2]
secondhalf = s1[len(s1)//2:]
out = firsthalf+s2+secondhalf

print(out)