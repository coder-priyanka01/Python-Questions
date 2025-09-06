# Write a program to take a list of numbers and remove all duplicate elements without using set().

numbers = [1, 2, 3, 4, 2, 3, 5, 1, 6]
unique_list = []

for n in numbers:
    if n not in unique_list:
        unique_list.append(n)

print("Original list:", numbers)
print("List without duplicates:", unique_list)

