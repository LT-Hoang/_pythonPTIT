
def tongPosChan(n):
    sum = 0
    for i in range(0, len(n), 2):
        sum += int(n[i])
    return sum

def tichPosLe(n):
    tich = 1
    ok = 0
    for i in range(1, len(n), 2):
        if int(n[i]) != 0:
            tich *= int(n[i])
            ok = 1
    if ok == 1:
        return tich
    else:
        return 0


t = int(input())
for _ in range(t):
    n = input()
    print(tongPosChan(n), end = " ")
    print(tichPosLe(n))

