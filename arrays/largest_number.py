from typing import List
from functools import cmp_to_key
import random

def largestNumber(nums: List[int]) -> str:
    res = nums[:]
    res.sort(key=cmp_to_key(lambda a, b: (a * 10**len(str(b)) + b) - (b * 10**len(str(a)) + a)))
    cnt = 0
    for i, num in enumerate(res):
        if num == 0:
            cnt += 1
        res[i] = str(num)
    return "".join(res[::-1]) if cnt != len(nums) else "0"


# test the function
# expected output: "210"
nums = [random.randint(0, 100) for i in range(10)]
print(nums)
print(largestNumber(nums))