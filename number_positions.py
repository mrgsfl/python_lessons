lst = [int(i) for i in input().split()]
index_list = []
x = int(input())
if x not in lst:
    print('Отсутствует')
else:
    for i, item in enumerate(lst):
        if item == x:
            index_list += [i]
print(*index_list)
