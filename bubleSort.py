def sort(arr, s_index):
    arr_t = arr
    if s_index == arr_t.__len__()-1:
        return arr_t
    
    for i in range(0, s_index):
        if i<s_index-1:
            if arr_t[i]>arr_t[i+1]:
                temp = arr_t[i]
                arr_t[i] = arr_t[i+1]
                arr_t[i+1] = temp
    
    return sort(arr_t, s_index+1)


a = input('n개의 데이터를 공백으로 구분해서 입력하세요.\n')
arr1 = a.split(' ')
arr2 = []

for i in arr1:
    arr2.append(int(i))

print(sort(arr2, 0))