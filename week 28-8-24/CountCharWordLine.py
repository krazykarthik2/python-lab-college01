# to count no of character, words and lines
para = "lorem ipsum dolor sitor amet, consectutor adipscing elit\n\
 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\
ut enim ad minim veniam, quis nostrud exercitation ullamco\n\
 laboris nisi ut aliquip ex ea commodo consequat."

words = para.split(' ')
lines = para.split('\n')

print("Number of characters: ", len(para))
print("Number of words: ", len(words))
print("Number of lines: ", len(lines))
