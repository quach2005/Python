A = float(input('Nhập số A: '))
n = 0
s = 0
while s<A:
	n+=1
	s+=1/n
	if s>A:
		print('Để 1+1/2+1/3+1/4+...1/n > A thì n = ',n)