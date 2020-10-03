in_list = []
with open('dataset_3363_2.txt', 'r') as inf:
    in_list += inf.readline().strip()
res = in_list[0]
tmp = in_list[1]
for i in range(2, len(in_list)):
    if in_list[i] >= 'A':
        res += res[-1] * (int(tmp) - 1) + in_list[i]
        tmp = ''
    elif in_list[i] < 'A':
        tmp += in_list[i]
res += res[-1] * (int(tmp) - 1)
with open('output.txt', 'w') as ouf:
    ouf.write(res)
