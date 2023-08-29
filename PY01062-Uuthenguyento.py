import math
def nto(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def check(n):
    if nto(len(n)):
        cnt = 0
        cnt2 = 0
        for i in range(0, len(n)):
            if nto(int(n[i])):
                cnt += 1
            else:
                cnt2 += 1
        if cnt2 > cnt: 
            return False
        return True
    return False

t = int(input())
for _ in range(t):
    n = input()
    if check(n) :
        print("YES")
    else:
        print("NO")