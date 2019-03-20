a = int(input())
b = int(input())

month = [31,28,31,30,31,30,31,31,30,31,30,31]

sum = 0

for i in range(0, a-2):
    sum += month[i]

sum += b

s = sum%7

if s == 4:
    print('SAT')
elif s ==5:
    print('SUN')
elif s ==6:
    print('MON')
elif s ==0:
    print('TUE')
elif s ==1:
    print('WED')
elif s ==2:
    print('THU')
elif s ==3:
    print('FRI')
