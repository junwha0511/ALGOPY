def solution(x):
    num = 0
    arr = [0,0,0,0,0]
    sum = 0
    for i in range(1,5):
        if num == x:
            break;
        else:
            arr[i-1]= (x%(10**i)-num)/10**(i-1)
            num += x%(10**i)-num
            sum+=arr[i-1]
    
    if x%sum==0:
        answer = True
    else:
        answer = False
    return answer

if solution(int(input())):
    print('harshard')
else:
    print('non-harshard')