n = int(input())
i = 1
lst = []
while len(lst) < n:
    lst += [i] * i
    i += 1
print(*lst[:n])
