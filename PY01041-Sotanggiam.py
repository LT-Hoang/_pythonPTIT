
def solve(s) :
    l = len(s)
    pos = 0
    if l < 3 : return False
    for i in range(0, len(s) - 1):
        if int(s[i]) == int(s[i + 1]) :
            return False
        if int(s[i]) - int(s[i + 1]) > 0 :
            pos = i
            break
    if pos == 0: 
        return False
    else :
        for i in range(pos, l - 1) :
            if(int(s[i]) - int(s[i + 1]) < 0):
                return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    if(solve(s) == True) :
        print("YES")
    else:
        print("NO")