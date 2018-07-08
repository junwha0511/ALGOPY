import math
a1 = float(input())
print(a1)
a2 = float(input()) 
print(a2)
a3 = float(input())
print(a3)

r1 = (a2/a1)
print(r1)
r2 = (a3/a2)
print(abs(r2-r1))


if int(r2-r1) == 0:
    print('등비수열 입니다.')
else:
    print('등비수열이 아닙니다.')