# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time Complexity: O(n)
def lengthOfLongestSubstring(s: str) -> int:
    end = len(s)
    lookup = set()
    start, no_dup_scan = 0, 0
    result = 0
    while no_dup_scan < end:
        # expand to the right until valid window of non duplicate string
        if s[no_dup_scan] not in lookup:
            lookup.add(s[no_dup_scan])
            result = max(result,(no_dup_scan-start)+1)
            no_dup_scan += 1
        else:
            lookup.remove(s[start])
            start += 1
    return result
    
if __name__ == '__main__':
    arr = "abcabcbb"
    print(lengthOfLongestSubstring(arr)) # 3