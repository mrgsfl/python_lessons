with open('dataset_3363_3.txt', 'r') as inf:
    input_list = list()
    for line in inf.readlines():
        input_list.extend(line.lower().strip().split(' '))
d = {}
d = {x: input_list.count(x) for x in input_list if x not in d}
amount = max(d.values())
words = []
for key, value in d.items():
    if value == amount:
        words.append(key)
with open('output.txt', 'w') as ouf:
    ouf.write(min(words) + ' ' + str(amount))
    
