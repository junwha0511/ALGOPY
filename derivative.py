line = int(input()) #라인 수 입력

sum = 0

for i in range(line): 
    numAndTerm = input().split(" ") #항의 계수와 차수 입력
    order = int(numAndTerm[1]) #차수
    term = int(numAndTerm[0]) #계수
    sum += (order*term*(2**(order-1))) #차수x계수x2의 차수-1 제곱

print(sum%1000000007)

