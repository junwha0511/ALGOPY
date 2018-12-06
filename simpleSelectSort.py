
def sort(s_index, arr):
    arr_t = arr
    if s_index == arr_t.__len__()-1:
        return arr_t
    m_index = s_index
    for i in range(s_index,arr_t.__len__()): #0~(len of arr)-1
        if arr_t[i]<arr_t[m_index]: # if min is arr[i]
            m_index = i
    
    temp = arr_t[m_index]
    arr_t[m_index] = arr_t[s_index]
    arr_t[s_index] = temp
    
    return sort(s_index+1,arr_t)

print('n개의 데이터를 공백으로 구분해서 입력하세요.')
arr1 = input().split(" ")
arr2 = []
min = 0 #최댓값이 저장될 변수
for i in arr1:
    num = int(i) #입력받은 데이터를 정수로 변환
    arr2.append(num) #arr2에 이동
    

print(sort(0, arr2))