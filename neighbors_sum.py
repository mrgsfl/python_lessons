a = [int(i) for i in input().split()]
res = []
if len(a) == 1:
    res = a
else:
    for i in range(len(a)):
        if i == len(a) - 1:
            res += [a[i - 1] + a[0]]
        else:
            res += [a[i - 1] + a[i + 1]]
print(*res) # распаковка списка: содержимое будет выведено без скобок []

