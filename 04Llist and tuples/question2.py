# Given a list of integers, separate even and odd numbers into two different lists.

nums = [10, 21, 4, 45, 66, 93, 11, 28]
even_list = []
odd_list = []

for n in nums:
    if n % 2 == 0:
        even_list.append(n)

    else:
        odd_list.append(n)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)