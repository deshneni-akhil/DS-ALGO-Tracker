def subset_generator(nums):
    result = []
    buffer = []
    def backtrack_dfs(index):
        if index == len(nums):
            result.append(buffer[:])
            return
        
        # include the current element
        buffer.append(nums[index])
        backtrack_dfs(index+1)

        # exclude the current element
        buffer.pop()
        backtrack_dfs(index+1)
    backtrack_dfs(0)
    print(result)
    

if __name__ == '__main__':
    nums = [1,2,3]
    subset_generator(nums) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]