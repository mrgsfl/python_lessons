a, b = (int(i) for i in input().split())
n = 0
s = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        s += i
        n += 1
print(s / n)
