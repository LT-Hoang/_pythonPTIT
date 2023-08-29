
t = int(input())
for i in range(t):
    s = input()
    l = len(s)
    tmp = ""
    for i in range(1, l):
        if s[i].isnumeric() :
            tmp += s[i - 1] * (int(s[i]))
    print(tmp)