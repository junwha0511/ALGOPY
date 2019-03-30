n = int(input())

arr = [0 for i in range(n+2)]
arr[1] = 1
arr[2] = 2

def sum(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    if arr[n-1]==0:
        arr[n-1] = sum(n-1)
    if arr[n-2]==0:
        arr[n-2] = sum(n-2)
    arr[n] = arr[n-1]+arr[n-2]
    return arr[n]
    
print(sum(n))