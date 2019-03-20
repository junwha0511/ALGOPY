
def getGCD(a, b):
    if a%b == 0:
        return b
    elif a%b >0:
        return getGCD(b,a%b)

a = int(input('두 정수를 입력하세요\n'))
b = int(input())

if a<b:
    l=b
    s=a
else:
    l=a
    s=b

print('최대공약수는 '+str(getGCD(l,s))+'입니다')
