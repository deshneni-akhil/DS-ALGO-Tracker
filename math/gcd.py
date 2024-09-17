def brute_force(a, b):
    min_val = min(a, b)
    for i in range(min_val, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1

def euclidean(a, b):
    if b == 0:
        return a
    return euclidean(b, a % b)

def gcd(a, b):
    # res = brute_force(a, b)
    res = euclidean(a, b)
    print(res)

# test the function
# expected output: 1
a = 18
b = 48
gcd(a, b)

# why does euclidean algorithm work?
# let's say a = 48 and b = 18
# 48 = 18 * 2 + 12
# 18 = 12 * 1 + 6
# 12 = 6 * 2 + 0
# 6 is the gcd of 48 and 18
# formula: a = b * q + r
# where q is the quotient and r is the remainder
# lets say d is the gcd of a and b
# d * x1 = a & d * x2 = b 
# d(x1 - x2) = a - b
# 6(8 - 3) = 48 - 18 = 30
