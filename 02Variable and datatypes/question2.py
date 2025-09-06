#Given: x = 10 and y = "20"
# A. what happens if you try x + y?
# B. why does it give an error?
# C. how can you fix it to make addition work?

x = 10
y = "20"
print(x + y)  # type: ignore

#This will raise a TypeError because you cannot add an integer (x) and a string (y) directly.

#To fix it, you can convert y to an integer using int(y) before adding:
#print(x + int(y))  # This will work and output 30
