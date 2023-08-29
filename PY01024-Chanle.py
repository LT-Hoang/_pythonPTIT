
def tong(n):
    sum = 0
    for i in range(n):
        sum += i
    if sum % 10 == 0 : return True
    return False

def check(n):
    for i in range(n) :
        if(abs(int(n[i]) - int(n[i + 1])) != 2) : return False
    return True

t = int(input())

for i in range(t):
    n = input()
    if tong(n) == True and check(n) == True :
        print("YES")
    else :
        print("NO")