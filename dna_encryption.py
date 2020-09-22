s = input()
res = ''
cnt = 1
if len(s) > 1:
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            res += s[i] + str(cnt)
            cnt = 1   
    res += s[i + 1] + str(cnt)
    print(res)
elif len(s) == 1:
    print(s + '1')
else:
    print('empty string')

