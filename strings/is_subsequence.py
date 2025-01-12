def isSubsequence(s: str, t: str) -> bool:
    p1, p2 = 0, 0
    while p1 < len(s) and p2 < len(t):
        if s[p1] == t[p2]:
            p1 += 1
            p2 += 1
        else:
            p2 += 1
    return p1 == len(s)

# test the function
# expected output: True
s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))