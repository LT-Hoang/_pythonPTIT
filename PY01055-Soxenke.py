
def check(s) :
    m = int(s[-1])
    for i in range(0, len(s), 2):
        if(int(s[i])!= m):
            return False
    return True

       

t = int(input())

for _ in range(t):
    n = input()
    if len(n) % 2 == 1:
        if n[0] != n[1] and check(n):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")        
