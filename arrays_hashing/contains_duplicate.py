from collections import Counter

def approach_1(nums, n):
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                return nums[i]

def approach_2(nums, n):
    lookup = set()
    for num in nums:
        if num not in lookup:
            lookup.add(num)
        else:
            return num 
        
def approach_3(nums, n):
    nums = sorted(nums)
    for i in range(n-1):
        if nums[i] == nums[i+1]:
            return nums[i]

def approach_4(nums, n):
    nums = Counter(nums)
    for key, value in nums.items():
        if value > 1:
            return key

def approach_5(nums, n):
    # considering if the numbers are within the range of n
    for num in nums:
        if nums[abs(num)-1] < 0:
            return abs(num)
        nums[num-1] *= -1

def approach_6(nums, n):
    # re arrange the values to thier original indexes and checks for infinte loop to see duplicate element
    for i in range(n):
        while nums[i] != i + 1:
            temp = nums[i]
            nums[i] = nums[nums[i] - 1]
            nums[temp-1] = temp
            if nums[i] == nums[nums[i] - 1]:
                return nums[i]

    for i in range(n - 1):
        if nums[i] == nums[i+1]:
            return nums[i]

def conatins_duplicate(nums):
    n = len(nums)
    # ans = approach_1(nums, n)
    # ans = approach_2(nums, n)
    # ans = approach_3(nums, n)
    # ans = approach_4(nums, n)
    # ans = approach_5(nums, n)
    ans = approach_6(nums, n)
    print(f'duplicate element {ans}')

if __name__ == '__main__':
    # arr = [2,3,4,4,1,5] 
    arr = [3,1,3,4,2]
    # arr = [3,3,3,3,3]
    # arr = [1,3,4,2,2]
    conatins_duplicate(arr)