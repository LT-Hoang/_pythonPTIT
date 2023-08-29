import math
def nto(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def checkNto(s):
    n = int(s[-4:])
    if(nto(n)):
        return True
    return False

t = int(input())
for _ in range(t):
    n = input()
    if(checkNto(n)):
        print("YES")
    else:
        print("NO")