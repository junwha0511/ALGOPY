direc = str(input())
arr = direc.split('/')
i=-1
while(True):
    i+=1

    if i>=arr.__len__():
        break

    if (arr[i] == '.') or (arr[i] == ''):
        del(arr[i])
        i-=1
    elif arr[i] == '..':
        del(arr[i])
        del(arr[i])
        i-=2

direc = "/"
for el in arr:
    direc+=el
    direc+='/'

print(direc)

