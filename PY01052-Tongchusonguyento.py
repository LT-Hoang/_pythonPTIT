import math
def nto(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def tongcs(n):
    sum = 0
    for i in range(0, len(n)):
        sum += int(n[i])
    return sum


t = int(input())
for _ in range(t):
    n = input()
    if(nto(tongcs(n))):
        print("YES")
    else:
        print("NO")

