from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)) :
        for j in range(i + 1, len(nums)) :
            sum = nums[i] + nums[j]
            if sum == target : twoNumber = [i, j]
    return twoNumber