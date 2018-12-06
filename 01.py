import math
a1 = float(input())
a2 = float(input()) 
a3 = float(input())

r1 = (a2/a1)
r2 = (a3/a2)


if int(r2-r1) == 0:
    print('등비수열 입니다.')
else:
    print('등비수열이 아닙니다.')