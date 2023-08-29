def timMin(s) :
    min_N = 10**12
    tmp = ""
    for i in s:
        if i.isdigit() :
            tmp += i
        elif tmp != "" and i.isalpha():
            min_N = min(int(tmp), min_N)
            tmp = ""
    return min_N

t = int(input())
for i in range(t) :
    s = input()
    print(timMin(s))