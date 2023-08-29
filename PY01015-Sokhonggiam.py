def check(s) :
    for i in range(1,len(s)):
        if int(s[i]) - int(s[i - 1]) < 0 : return False
    return True

t = int(input())
for i in range(t) :
    s = input()
    if check(s) == True : 
        print("YES")
    else :
        print("NO")