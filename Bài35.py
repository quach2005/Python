n=[]
while True:
	b=int(input('Nhập số dương: '))
	n.append(b)
	if b<0:
		print('Số lớn nhất là',max(n))
		break