a = [int(i) for i in input().split()]
res = []
a.sort()
for i in range(len(a) - 1):
    if a[i] != a[i + 1]:
        continue
    elif a[i] not in res:
        res += [a[i]]
print(*res)
