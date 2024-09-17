import math

def gcdOfStrings(str1: str, str2: str) -> str:
    n, m = len(str1), len(str2)
    # edge case
    if n == m and str1 == str2:
        return str1
    observe = set(str1)
    for char in str2:
        if char not in observe:
            return ""
    # core logic
    small = str1 if n <= m else str2
    while small:
        if check(small, str1) and check(small, str2):
            return small
        small = small[0:len(small)-1]
    return ""

def check(rept, string):
    if len(string) % len(rept):
        return False
    return rept * (len(string)//len(rept)) == string

# time complexity: O(log(N) + N) Space complexity: O(1)
def optmized(str1: str, str2: str):
    if str1 + str2 != str2 + str1:
        return ""
    return str1[:math.gcd(len(str1), len(str2))]

# test the function
# expected output: "ABC"
str1 = "ABCABC"
str2 = "ABC"
# print(gcdOfStrings(str1, str2)) 
print(optmized(str1, str2)) 


# Analogy
# GCD of strings

# a greatest common string which can be multiped enough to create both the strings a & b 

# Idea:

# example: 
# A: ABABAB
# B: AB

# core solve: 
# Incrementing approach and reduction approach 

# n = len(a) m = len(b)

# Incrementing:
# We take pointers p1 & p2 and if both matches we take that char and store it in (check) and repeat it by n and m times if it matches we can return this check and we continue to append the char and check the process.

# Difficulity:
# Incrementing and appending is good however it may return lcd instead of gcd for reference consider this example:

# S1= ABABABAB
# S2 = ABAB

# with incrementing AB will give the answer as we multipy it enough how ever the gcd here is ABAB

# reduction: 
# Instead of incrementing the pointers can we take least string in size and try to reduce it by one chat and repeat and check if can give our gcd ? 

# with above example it gives answer in one shot

# Alt example:
# S1 = ABABAB
# S2 = ABAB

# ABAB 
# ABA reduced by 1 char
# AB reduced by 1 char ==> answer 

# Outlier:
# what makes to consider a string is not correct:
# if both strings has any one char thats not in common therefore we can't get gcd & if they do contain common characters if smallest string cant conjuct/lap with larger string.

# time complexity:
# set logic has a run time O(N)
# reptiosn string size m * (k (amount of times this string to get repeated))

# reptiton time complexity O(N) +  O(N to check two strings) * M 
# 
# Overall time complexity O(M * (M + N)) 



