def combinationSum(nums, target):
    result = []
    track_buff = []
    def backtrack(idx, curr_sum):
        if idx >= len(nums) or curr_sum > target:
            return
        if curr_sum == target:
            result.append(track_buff[:])
        
        if curr_sum + nums[idx] <= target:
            track_buff.append(nums[idx])
            backtrack(idx, curr_sum+nums[idx])

            track_buff.pop()
            backtrack(idx+1, curr_sum)
    
    nums.sort()
    backtrack(0, 0)
    return result

if __name__ == '__main__':
    nums = [2,5,6,9]
    target = 9
    res = combinationSum(nums, target)
    print(res)