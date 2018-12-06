stack = []

def push (a ):
 stack.insert(0 ,a)

def pop ():
 	a = stack[len (stack)-1]
	del stack[len (stack)-1]
	return a

push("제호")
push("재훈")
push("인준")
push("지아")

print (pop())
print (pop())