from bisect import bisect_left, bisect_right
import random

class BinarySearch:
    def __init__(arr):
        self.arr = arr
    
    def search(target):
        low, high = 0, len(self.arr)
        while low < high:
            mid = low + ((high - low) // 2)
            if self.arr[mid] == target:
                if self.arr.index(target) != mid:
                    print('custom binary search:', mid, 'py binary search:', self.arr.index(target))
                    print('observation of low and high:', low, high)
                return mid
            elif self.arr[mid] > target:
                high = mid
            else:
                low = mid + 1
        return -1

    def search_left(target):
        left, right = 0, len(self.arr)

        if target is None:
            raise ValueError('target is None')
        
        while left < right:
            mid = (left + right) >> 1
            if self.arr[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        py_bisect = bisect_left(self.arr, target)
        
        if left != py_bisect:
            print('custom bisect_left:', left, 'py bisect_left:', py_bisect)
            print('observation of low and high:', left, right)
        return left
    
    def search_right(target):
        left, right = 0, len(self.arr)

        if target is None:
            raise ValueError('target is None')
        
        while left < right:
            mid = (left + right) >> 1
            if self.arr[mid] <= target:
                left = mid + 1
            else:
                right = mid

        py_bisect = bisect_right(self.arr, target)
        if left != py_bisect:
            print('custom bisect_right:', left, 'py bisect_right:', py_bisect)
            print('observation of low and high:', left, right)
        return left


if __name__ == '__main__':
    b = BinarySearch([1,4,5,6,7,9])
    # b = BinarySearch([1,3,5,7,7,7,11,12,15])
    
    # test zone 
    # print(b.search(15)) # 4
    print(b.search_left(3))
    # print(b.search_right(2))
    
    
    # experiment zone 
    # for _ in range(int(1e2)):
    #     rand = random.randint(1, 16)
    #     print('target:', rand)
    #     b.search(rand)
    