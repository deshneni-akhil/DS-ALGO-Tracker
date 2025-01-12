from typing import List

def maxArea_1(height: List[int]) -> int:
    # brute force tc: O(n^2) sc: O(1)
    max_area_ans = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            max_area_ans = max(max_area_ans, min(height[i],height[j]) * (j - i))
    return max_area_ans

def maxArea2(height: List[int]) -> int:
    # two pointer approach tc: O(n) sc: O(1)
    max_area_ans = 0
    p1, p2 = 0, len(height) - 1
    while p1 < p2:
        max_area_ans = max(max_area_ans, min(height[p1], height[p2]) * (p2 - p1))
        if height[p1] < height[p2]:
            p1 += 1
        else:
            p2 -= 1
    return max_area_ans

# test the function
# expected output: 49
height = [1,8,6,2,5,4,8,3,7]
print(maxArea_1(height))
