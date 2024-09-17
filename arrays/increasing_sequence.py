# Write a function that takes in an array of integers and returns whether there exists an increasing sequence of length 3 in the array.

# time complexity: O(N) and space complexity: O(1)
def increasing_triplet_sequence(arr):
    if not arr:
        return False
    first = second = float('inf')
    for num in arr:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False

# Follow up: can you find an increasing sequence of length k in the array?
'''
Analogy:
1. If k = 3, we can use the same approach as above but what if k is greater 

the quick idea comes to mind is to use heap sort and return the first k elements what if I say that the order shouldnt be changed like I need increasing sequences by indexes 

oops the above approach doesnt work and if we can use if elif statement we have a long chain of elif statements until k-1 this doesnt make much sense to solve the problem


example:

[2,3,1,4,2,5,7,8,9]

expected output: 1, 2, 5, 7, 8, 9
Quick solve: LIS 

however can I extend above problem to solve this problem ?

what if I can take an array of size k and initilaize them to [float('inf')] * k

while going through the array check array k from left to right and adjust elements accordingly and in the end we will have elements of size m where m can be m <= k 

'''

def extended_triplet_solve(nums, k):
    # time complexity: O(N * k + klog(k)) and space complexity: O(k)
    out = [(float('inf'), -1)] * k  # (value, index)
    m = 0  # keeps track of the last updated index in the 'out' array
    
    for idx, num in enumerate(nums):
        for i in range(k):
            # Only update if the current number is smaller than the last used element
            if num <= out[i][0]:
                out[i] = (num, idx) 
                # print(out, '===>', num, f"at index {idx}")
                m = max(m, i)  
                break
    out = out[:m + 1]
    out.sort(key=lambda x: (x[1], x[0]))
    print(f"Increasing sequence for {k} elements found {m + 1} increasing elements: {[x[0] for x in out]}")
    return out

# Test the function
arr = [6, 9, 8, 1, 4, 1, 3, 2, 4, 7, 9, 2, 9, 9, 9, 8, 9, 7, 5, 5, 5]
print(increasing_triplet_sequence(arr)) # expected output: True

## experiment for extended solve
extended_triplet_solve(arr, 9) # expected output: [1, 2, 4, 7, 9, 5]