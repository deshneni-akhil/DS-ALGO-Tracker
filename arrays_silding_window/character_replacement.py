# Problem: Longest Repeating Character Replacement (LeetCode 424)
def characterReplacement(s: str, k: int) -> int:
    frequency = [0]*26
    max_window = 0
    left = right = 0
    max_freq = 0
    while right < len(s):
        frequency[ord(s[right])-ord('A')] += 1
        max_freq = max(max_freq, frequency[ord(s[right])-ord('A')])
        if right - left + 1 > max_freq + k:
            frequency[ord(s[left])-ord('A')] -= 1
            left += 1
        right += 1
    print(right,' ',left)
    return right - left

if __name__ == '__main__':
    arr = "ABBAB"
    print(characterReplacement(arr, 2)) # 4