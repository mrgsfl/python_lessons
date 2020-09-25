result = 0
lst = []
total = int(input())
lst.append(total)
while total != 0:
    i = int(input())
    lst.append(i)
    total += lst[-1]
for c in lst:
    result += c * c
print(result)
    
               
