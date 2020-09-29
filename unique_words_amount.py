input_list = [str(i) for i in input().split()]
d = {}
input_list[:] = [x.lower() for x in input_list]
d = {x: input_list.count(x) for x in input_list if x not in d}
for key, value in d.items():
    print(key, value)
