a=10
b=(x for x in range(a))
c=0
while c<a:
	print(next(b))
	c+=1