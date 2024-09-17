from typing import List
import math

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        # if no flowers then return true
        if n == 0:
            return True
        # if array size is one 
        if m == 1:
            return flowerbed[0] == 0 and n <= 1
        # checking if I have enough beds to place flowers
        if n > m or math.ceil((m - sum(flowerbed))/2):
            return False
        # arraqy size is atleast 2 we can proceed with algorithm
        for i in range(m):
            if (i == 0 and flowerbed[i] == 0) and (i + 1 < m and flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
            elif (flowerbed[i] == 0 and flowerbed[i-1] == 0) and (i + 1 < m and flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
            elif (i == m - 1 and flowerbed[i] == 0) and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0

# test the function
flowerbed = [1,0,0,0,1]
n = 1
print(canPlaceFlowers(flowerbed, n)) # True

# Analogy
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# example: 
# flowerbed = [1,0,0,0,0,1]
# n = 2

# Thought process:

# Formal case:
# case-1: A flower can be placed in flowerbed if and only if its behind and next were 0's which means empty
# case-2: A flower can be placed in the beginning only if there is next splot free 
# case-3: A flower can be placed in the end if its behind spot is free

# Outliers/ edge cases:
# if n is 0 then return True
# if size of n is greater or w.r.t. size of flowerbed - sum of flowers than the available capacity then we cant place flowers return false
# try to place the flowers from begging so that we can maximixe the placements of flowers (greedy approach)
# to place a flower I need atleast 2 empty spots therefore as per math ceil I need atleast (m - sum(flowerbed))//2 empty spots to place flowers

# Over-optimization: (Wrong Answer)
# test-case: 0 n = 1
# n > ((m - sum(flowerbed))//2) returns False

