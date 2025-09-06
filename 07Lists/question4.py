nums = [10, 25, 18, 40, 32]

first = second = float("-inf")

for n in nums:
    if n > first:
        second = first
        first = n

    elif n > second and n != first:
        second = n

print("Second Greatest Element:", second)
