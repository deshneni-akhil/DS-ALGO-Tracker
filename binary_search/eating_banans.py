from typing import List
from math import ceil

def minEatingSpeed(piles: List[int], h: int) -> int:
    target = max(piles)
    low, high = 1, target
    res = high
    while low <= high:
        mid = low + ((high - low) // 2)
        eating_speed = calculate_eating_speed(piles, mid)
        if eating_speed >= h:
            low = mid + 1
            res = mid
        else:
            high = mid - 1
    return res 

def calculate_eating_speed(piles: List[int], speed: int) -> int:
    hours = 0
    for pile in piles:
        hours += ceil((pile) / speed)
    return hours

piles = [25,10,23,4]
# piles = [3,6,7,11]
h = 4
print(minEatingSpeed(piles, h)) # 25
