#장점: 처리가 간단하다.
#단점: 사용되는 자원의 크기가 크다

print('n개의 데이터를 공백으로 구분해서 입력하세요.')
arr1 = input().split(" ")
arr2 = []
max = 0 #최댓값이 저장될 변수
for i in arr1:
    num = int(i) #입력받은 데이터를 정수로 변환
    arr2.append(num) #arr2에 이동
    if num>max:
        max = num

arr3 = [-1]*(max+1) #인덱스가 arr2의 값이 되는 배열
for i in arr2:
    arr3[i] = 1 #arr2의 데이터와 일치하는 arr3의 인덱스의 데이터를 1로 지정

arr4 = [] #정렬된 배열
for i in range(max+1):
    if arr3[i] == 1:
        arr4.append(i)

print(arr4)