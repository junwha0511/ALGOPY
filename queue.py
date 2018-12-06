queue= []

def push (a ):
 queue.append(a)

def pop ():
 	a = queue[0]
	del queue[0]
	return a

push("제호")
push("재훈")
push("인준")
push("지아")

print (pop())
print (pop())