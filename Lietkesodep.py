
def checkcs(n) :
    for i in range(1, len(n)) :
        if (n[i] != 0 and n[i] != 2 and n[i] != 4 and n[i] != 6 and n[i] != 8):
            return False
        

t = int(input())

for i in range(t) :
    n = input()


