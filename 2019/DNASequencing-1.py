n = int(input())
a = list(input())
d = [[0,2,0,1],[2,1,3,0],[0,3,2,1],[1,0,1,3]]
def I(d):
    if d=='A':
        return 0
    elif d=='G':
        return 1
    elif d=='C':
        return 2
    elif d=='T':
        return 3 
a = list(map(lambda x: I(x),a))
while n>1:    
    a[n-2]=d[a[n-1]][a[n-2]]
    del a[n-1]
    n-=1
k=a[0]
if k==0:
    print('A')
elif k==1:
    print('G')
elif k==2:
    print('C')
elif k==3:
    print('T')