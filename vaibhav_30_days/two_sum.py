from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = []
    for i in range(len(nums)):
        if (target - nums[i]) in seen:
            print([i, nums.index(target - nums[i])])
            return [i, nums.index(target - nums[i])]
        else:
            seen.append(nums[i])


two_sum([2, 7, 11, 15], 9)
