import math
def nto(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
def check(n):
    for i in range(len(n)):
        if(nto(i)!= nto(int(n[i]))):
            return False
    return True
        
t = int(input())
for _ in range(t) :
    n = input()
    if(check(n)):
        print("YES")
    else:
        print("NO")