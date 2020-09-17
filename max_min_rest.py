maxnum = int(input())
minnum = int(input())
rest = int(input())
if maxnum < minnum: 
    (maxnum, minnum) = (minnum, maxnum)
    if maxnum < rest:    
        (maxnum, rest) = (rest, maxnum)
        print('max', maxnum, '\nmin', minnum, '\nrest', rest)
    elif minnum > rest:               
        (minnum, rest) = (rest, minnum)
        print('max', maxnum, '\nmin', minnum, '\nrest', rest)
    else:
        print('max', maxnum, '\nmin', minnum, '\nrest', rest) 
elif maxnum < rest:
    (maxnum, rest) = (rest, maxnum)
    print('max', maxnum, '\nmin', minnum, '\nrest', rest)
elif minnum > rest:
    (minnum, rest) = (rest, minnum)
    print('max', maxnum, '\nmin', minnum, '\nrest', rest)
else:
    print('max', maxnum, '\nmin', minnum, '\nrest', rest)   



