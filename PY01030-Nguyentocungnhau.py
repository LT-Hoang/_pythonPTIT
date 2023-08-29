import math
def uocChung(a, b) :
    return math.gcd(a, b)

x = 1
n, k = [int(x) for x in input().split()]
for i in range(10**(k-1), 10**k) :
    if uocChung(i, n) == 1:
        print(i, end = ' ')
        if x % 10 == 0:
            print()
        x += 1