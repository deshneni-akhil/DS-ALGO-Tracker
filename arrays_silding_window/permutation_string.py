from collections import defaultdict, Counter

# Approach 1: Sliding Window and time complexity is O(N^2) and space complexity is O(1)
def approach_1(s1, s2):
    count_s1 = Counter(s1)
    left = 0
    while left < len(s2):
        curr_char = s2[left]
        if curr_char in count_s1:
            right = left
            freq = defaultdict(int)
            while right < len(s2) and s2[right] in count_s1:
                freq[s2[right]] += 1
                right += 1
                if isPermutation(freq, count_s1):
                    # print(left,'===',right)
                    return True
            left = right if right < len(s2) else left
        left += 1
    return False

# uses sorting and time complexity is O(MlogM*N) and space complexity is O(1)
def appraoch_2(s1, s2):
    seq1 = ''.join(sorted(s1))
    left = 0
    while left < len(s2):
        seq2 = ''.join(sorted(s2[left:left+len(s1)]))
        if seq1 == seq2:
            return True
        left += 1
    return False

# uses sliding window and time complexity is O(N) and space complexity is O(1)
def appraoch_3(s1, s2):
    s1_map = [0]*26
    s2_map = [0]*26
    for i in range(len(s1)):
        s1_map[ord(s1[i])-ord('a')] += 1
        s2_map[ord(s2[i])-ord('a')] += 1
    
    for i in range(len(s2)-len(s1)):
        if(matches(s1_map, s2_map)):
            return True 
        s2_map[ord(s2[i + len(s1)])-ord('a')] += 1
        s2_map[ord(s2[i])-ord('a')] -= 1

    return matches(s1_map, s2_map)


def checkInclusion(s1: str, s2: str, function: object) -> bool:
    if len(s1) > len(s2):
        return False
    return function(s1, s2)


def matches(s1, s2):
    return all(s1[i] == s2[i] for i in range(26))

def isPermutation(freq, count_s1):
    for key, value in count_s1.items():
        if freq[key] != value:
            return False
    return True
            
if __name__ == '__main__':
    functions = [approach_1, appraoch_2, appraoch_3]
    function = functions[2]
    s1 = "ab"
    s2 = "eidbaooo"
    print(checkInclusion(s1, s2, function)) # True
    s1 = "ab"
    s2 = "eidboaoo"
    print(checkInclusion(s1, s2, function)) # False
    s1 = "adc"
    s2 = "dcda"
    print(checkInclusion(s1, s2, function)) # True
    s1 = "hello"
    s2 = "ooolleoooleh"
    print(checkInclusion(s1, s2, function)) # False
