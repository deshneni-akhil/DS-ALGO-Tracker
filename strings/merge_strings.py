def mergeAlternately(word1: str, word2: str) -> str:
    p1, p2 = 0, 0 
    n1, n2 = len(word1), len(word2)
    result = ''
    while p1 < n1 and p2 < n2:
        if word1[p1] and word2[p2]:
            result += word1[p1]
            result += word2[p2]
        p1 += 1
        p2 += 1
    if p1 < n1:
        result += word1[p1:]
    else:
        result += word2[p2:]
    return result
    
word1 = "abc"
word2 = "pqr"
print(mergeAlternately(word1, word2)) # apbqcr