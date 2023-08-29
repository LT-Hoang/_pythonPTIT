def check(s):
    n = len(s)
    for i in range(2, n) :
        if s[i] != s[i - 2] : return False
    return True      


t = int(input())

for j in range(t) :
    s = input()
    if check(s) == True :
        print("YES")
    else :
        print("NO")