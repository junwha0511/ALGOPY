#P(i) => i장의 카드팩
#P(i)=C일 때 한장당 가격 = C/i
#가격대 별로 분류하고 가장 높은 가격인 것들로 4개 구성

n = int(input()) #민규가 구매하려고 하는 카드의 개수

cards = input().split(' ') #P(1)~P(n)까지의 카드팩 가격
costs = [] #한 장 당 가격이 저장될 곳

for i in range(len(cards)):
    cards[i] = int(cards[i]) #카드 가격을 STR형에서 INT형으로 변환

if n<=len(cards):
 cards = cards[0:n] #n장의 카드를 구매하므로 n장 이상의 카드팩은 제외

index = [0]*len(cards)
for i in range(len(cards)):
    costs.append(cards[i]/(i+1)) #해당 팩의 한장당 가격 저장
    index[i]=i #가격에 대응하는 팩의 장수

#버블소트로 오름차순으로 정렬
length = len(costs)
for i in range(length-1):
    for j in range(length-i-1):
        if costs[j]<costs[j+1]:
            costs[j+1],costs[j]=costs[j],costs[j+1] 
            index[j+1],index[j]=index[j],index[j+1]

rest = n #초기 나머지를 구매하고자 하는 카드 개수로 설정
sum = 0 #가격의 총합
for i in range(len(costs)):
    if not (rest%(index[i]+1) == n): #나머지를 카드 개수로 나누었을 때 n이 아니라면(=카드 개수가 rest보다 작거나 같다면)
        sum+=cards[index[i]]*(rest//(index[i]+1)) #가격의 총합에 (구매하는 팩의 카드 장 수)*(구매하는 카드 팩 수)를 더한다
        rest = rest%(index[i]+1) #나머지를 갱신한다.
    if rest%(index[i]+1) == 0: #카드개수로 나머지를 나누었을 때 0이라면
        print(sum) #결과값을 출력하고 
        break #for문을 닫는다.












