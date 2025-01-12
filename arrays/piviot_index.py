from typing import List

def pivotIndex_1(nums: List[int]) -> int:
    # proceed with the case having an array with atleast three elements tc: o(N ^ 2)
    for i in range(len(nums)):
        left, right = sum(nums[:i]), sum(nums[i+1:])
        if left == right:
            return i 
        elif 0 == right and 0 == left:
            return i
    return -1

