def demcs(s) :
    n = int(s)
    cnt = 0
    while n > 0 :
        cnt += 1
        n /= 10
    return cnt % 2 == 0

def check(s) :
    n = len(s)
    for i in range(n) :
        if (s[i] != s[n - i - 1]) and (s[i] != '0' and s[i] != '2' and s[i] != '4' and s[i] != '6' and s[i] != '8') :
            return False
    return True



t = int(input())
for i in range(t) :
    s = input()
    n = int(s)
    for i in range(n) :
        if (demcs(i) == True) and (check(s) == True) :
            print(i)

    