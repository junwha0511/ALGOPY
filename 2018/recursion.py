def rec(a):
    if a<10:
        return rec(a+1)
    if a==10:
        return a

print(rec(6))
#rec(1)
#rec(2)
#rec(3)
#rec(4)
#rec(10)