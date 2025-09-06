"""Create three variables:
. a = 5
. b = 2.0
. c = "5"
compare:
. a == b
. a == c
and explain the output ?"""

a = 5
b = 2.0 
c = "5"

print(a == b)  # False, because a is an integer and b is a float
print(a == c)  # False, because a is an integer and c is a string