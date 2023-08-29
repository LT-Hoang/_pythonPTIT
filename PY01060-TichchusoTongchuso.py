
def tichcs(s) :
    l = len(s)
    tich = 1
    for i in range(0, l, 2) :
        if s[i] != '0' :
            tich = tich * int(s[i])
    return tich

def tongcs(s) :
    l = len(s)
    sum = 0
    for i in range(1, l, 2) :
        sum += int(s[i])
    return sum

t = int(input())
for i in range(t):
    s = input()
    print(str(tichcs(s)) + " " + str(tongcs(s)) )