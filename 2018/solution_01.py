#세 수를 입력받고, 세 수가 입력받은 순서대로 등차수열을 이루면 True를, 등차수열을 이루지 않으면 False를 출력하시오.
print('세 수를 입력하세요\n')
a1 = int(input())
a2 = int(input())
a3 = int(input())

if (a1+a3)/2 == a2:
    print('등차수열입니다.')
else:
    print('등차수열이 아닙니다.')