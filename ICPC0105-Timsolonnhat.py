def timMax(s) :
    tmp = ""
    max_N = -10**12
    for i in s:
        if i.isdigit():
            tmp += i
        elif i.isalpha() and tmp != "":
            max_N = max(int(tmp), max_N)
            tmp = ""
    if tmp != "":
        max_N = max(int(tmp), max_N)
    return max_N
t = int(input())
for i in range(t) :
    s = input()
    print(timMax(s))
