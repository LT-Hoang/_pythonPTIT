ds1 = [1, -3, -17, 0, -100, 6]
ds2 = sorted(ds1)
print(ds2)
sum = ds2[0]
ds3 = []
for i in range(len(ds2)):
    if sum + int(ds2[i]) < sum:
        ds3.append(ds2[i])
print(ds3)