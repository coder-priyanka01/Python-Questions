nums = [1, 2, 3, 4, 5]

is_sorted = True
for i in range(len(nums)-1):

    if nums[i] > nums[i+1]:
        is_sorted = False
        break

if is_sorted:
    print("List is Sorted")
    
else:
    print("List is NOT Sorted")
