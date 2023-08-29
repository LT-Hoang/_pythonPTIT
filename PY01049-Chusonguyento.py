import math
def nto(n) :
    if n < 2: return False
    for i in range(2, n//2 +1):
        if n % i == 0: return False
    return True

# def check(n) :
#     s = str(n)
#     l = len(s)
#     cnt1 = 0
#     while n > 0:
#         if nto(n % 10) == True:
#             cnt1 += 1
#         n /= 10
#     cnt2 = l - cnt1
#     return cnt1 - cnt2

t = int(input())

for i in range(t):
    n = input()
    if nto(len(n)):
        cnt1 = 0
        cnt2 = 0
        for i in range(0, len(n)):
            if nto(int(n[i])):
                cnt1 += 1
            else :
                cnt2 += 1
        if(cnt1 > cnt2) :
            print("YES")
        else:
            print("NO")
    else :
        print("NO")