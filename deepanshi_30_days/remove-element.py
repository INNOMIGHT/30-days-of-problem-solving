def removeElements(nums, val):
    j = 0
    for i in  range(len(nums)):
        if(nums[i] != val):
            nums[j] = nums[i]
            j = j + 1
    return j

print(removeElements([3,2,2,3], 3))