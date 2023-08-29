import math
def nto(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return 1

t = int(input())
for i in range(t):
    n = input()
    a = int(n[0:3:1])
    b = int(n[-3:])
    if(nto(a) and nto(b)):
        print("YES")
    else:
        print("NO")