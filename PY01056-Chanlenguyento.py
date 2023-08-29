import math
def nto(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def tongcs(n) :
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum

def check(s):
    for i in range(0, len(s)):
        if i % 2 == 0 and int(s[i]) % 2 != 0:
            return False
        elif i % 2 != 0 and int(s[i]) % 2 == 0:
            return False
    return True

t = int(input())
for i in range(t):
    n = input()
    if check(n) and nto(tongcs(n)):
        print("YES")
    else:
        print("NO")

