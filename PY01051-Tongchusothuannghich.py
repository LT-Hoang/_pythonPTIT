def thuanNghich(s) :
    if len(s) < 2 : return False
    if s[::-1] != s[::1] : return False
    return True

def tongCs(s) :
    l = len(s)
    sum = 0
    for i in range(0, l) :
        sum += int(s[i])
    return str(sum)

t = int(input())
for i in range(t):
    n = input()
    if thuanNghich(tongCs(n)) == True:
        print("YES")
    else:
        print("NO")