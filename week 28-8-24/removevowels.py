import re as regex;

s=input("Enter a string:")
# remove all vowels
s = regex.sub('[aeiouAEIOU]', '', s)
print("USING REGEX:", s)
vowels  = 'aeiouAEIOU'

# remove all vowels
s = ''.join([char for char in s if char not in vowels])
print("WITHOUT REGEX:", s)