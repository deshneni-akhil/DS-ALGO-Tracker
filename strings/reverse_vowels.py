def reverseVowels(s: str) -> str:
    # time complexity: O(N) Space complexity: O(N)
    record = []
    for i, c in enumerate(s):
        if c in 'aeiouAEIOU':
            record.append((i, c))
    p1, p2 = 0, len(record) - 1
    while p1 < p2:
        record[p1] , record[p2] = (record[p1][0], record[p2][1]) , (record[p2][0], record[p1][1])
        p1, p2 = p1 + 1, p2 -1
    result = []
    idx = 0
    for i, c in enumerate(s):
        if idx < len(record) and i == record[idx][0]:
            result.append(record[idx][1])
            idx += 1
        else:
            result.append(c)
    return ''.join(result)

# time complexity: O(N) Space complexity: O(1)
def reverseVowels_optimized(s):
    vowels = set(list("aeiouAEIOU"))
    s = list(s)
    ptr_1, ptr_2 = 0, len(s) - 1
    while ptr_1 < ptr_2:
        if s[ptr_1] in vowels and s[ptr_2] in vowels:
            s[ptr_1], s[ptr_2] = s[ptr_2], s[ptr_1]
            ptr_1 += 1
            ptr_2 -= 1
        if s[ptr_1] not in vowels:
            ptr_1 += 1
        if s[ptr_2] not in vowels:
            ptr_2 -= 1
    return ''.join(s)

# test the function
# expected output: "holle"
s = "hello"
print(reverseVowels(s))
print(reverseVowels_optimized(s))