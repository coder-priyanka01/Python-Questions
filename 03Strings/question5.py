# write a program to find the first non-repeating character in a string.

text = "aabbcdde"

for char in text:
    if text.count(char) == 1:
        print("The first non-repeating character is:", char)
        break