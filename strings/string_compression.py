from typing import List

class string_compression:
    def compress(self, chars: List[str]) -> int:
        p1, p2 = 0, 0 
        p2_past = 0
        n = len(chars)
        while p2 < n:
            curr = chars[p2]
            p2 = self.findsequence(curr, p2 + 1, n, chars)
            comp_len = self.string_size(p2_past, p2)
            p2_past = p2
            p1 += 1
            for num in comp_len:
                chars[p1] = num
                p1 += 1
            if p2 < n:
                chars[p1] = chars[p2] 
        return p1
    
    def findsequence(self, letter, p2, n, chars):
        while p2 < n and chars[p2] == letter:
            p2 += 1
        return p2
    
    def string_size(self, p1, p2):
        num = (p2 - p1) 
        temp = []
        if num < 2:
            return temp
        while num:
            temp.append(num % 10)
            num = num // 10
        temp = [str(num) for num in temp]
        return temp[::-1]
    
# test the function
sc = string_compression()
chars = ["a","a","b","b","c","c","c"]
res = sc.compress(chars) # expected output: 6
print(chars[:res])

        
            
        