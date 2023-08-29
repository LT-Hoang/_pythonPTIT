import math
def nguyento(n) :
    if n < 2 : 
        return False
    for i in range(2,int(math.sqrt(n)) + 1) :
        if n % i == 0 : 
            return False
    return True

def uocchung(a, b) :
    return math.gcd(a, b)

def tong(a) :
    sum = 0
    while a > 0: 
        sum += a % 10
        a //= 10
    return sum

t = int(input())
for i in range(t) :
    a, b = [int(x) for x in input().split()]
    if nguyento(tong(uocchung(a, b))):
        print("YES")
    else:
        print("NO")
