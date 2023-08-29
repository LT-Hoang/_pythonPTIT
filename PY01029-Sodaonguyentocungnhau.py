import math

t = int(input())
for i in range(t):
    n = input()
    s = int(n[::-1])
    if math.gcd(int(n), s) == 1 :
        print("YES")
    else :
        print("NO")




