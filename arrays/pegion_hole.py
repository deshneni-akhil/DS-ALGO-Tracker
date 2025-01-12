'''
In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1. Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making the list longer than usual.

As the town detective, your task is to find these two sneaky numbers. Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.

2 <= n <= 100
nums.length == n + 2
0 <= nums[i] < n
The input is generated such that nums contains exactly two repeated elements.
'''

from typing import List

def getSneakyNumbers(nums: List[int]) -> List[int]:
    ans = []
    n = len(nums)
    for idx in range(n):
        ptr = idx
        # The idea is to swap the numbers to their correct index until the number at the index is equal to the index
        while nums[ptr] != idx:
            # If the number at the index same as the number at the desitnation index, then we have found the sneaky number
            if nums[ptr] == nums[nums[ptr]]:
                break
            temp = nums[ptr]
            nums[ptr] = nums[nums[ptr]]
            nums[temp] = temp
    for idx in range(n):
        if nums[idx] != idx:
            ans.append(nums[idx])
    return ans

# Time complexity: O(n)
# Space complexity: O(1)

# Test cases
assert len(set(getSneakyNumbers([2, 3, 1, 0, 2, 3])) & set([2, 3])) == 2
assert len(set(getSneakyNumbers([7,1,5,4,3,4,6,0,9,5,8,2])) & set([4, 5])) == 2
