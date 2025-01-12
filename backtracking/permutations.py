result = []

def permutations(nums, buffer):
    if len(buffer) == len(nums):
        result.append(buffer.copy())
        # print(result)
        return 
    
    for num in nums:
        if num not in buffer:
            permutations(nums, buffer+[num])
    
    return 

if __name__ == '__main__':
    nums = [1,2,4,6,7,8,9]
    permutations(nums, [])
    print(result)
