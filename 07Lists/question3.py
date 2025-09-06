nums = [5, 17, 9, 23, 15]

greatest = nums[0]
index = 0

for i in range(len(nums)):
    if nums[i] > greatest:
        greatest = nums[i]
        index = i

print("Greatest Element:", greatest)
print("Index:", index)
