a=[]
while True:
	b=int(input('Nhập vào số nguyên n: '))
	a.append(b)
	if b<0:
		a.remove(a[-1])
		print('n có ',len(a),'chữ số')
		break