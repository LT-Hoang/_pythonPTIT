t = int(input())
for i in range(t) :
    n = input()
    tich = 1
    for i in n :
        if i != '0' :
            tich *= int(i)
    print(tich)