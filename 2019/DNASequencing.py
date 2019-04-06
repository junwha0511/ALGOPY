n = int(input())
dna = list(input())

#A=0, G=1, C=2 T=3
data = [[0,2,0,1],[2,1,3,0],[0,3,2,1],[1,0,1,3]]

def dnaToIndex(d):
    if d=='A':
        return 0
    elif d=='G':
        return 1
    elif d=='C':
        return 2
    elif d=='T':
        return 3 

for i in range(n):
    dna[i] = dnaToIndex(dna[i])

while n>1:    
    x = dna[n-1]
    y = dna[n-2]
    dna[n-2]=data[x][y]
    del dna[n-1]
    n-=1
    
d=dna[0]

if d==0:
    print('A')
elif d==1:
    print('G')
elif d==2:
    print('C')
elif d==3:
    print('T')
