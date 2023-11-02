a=[]
b=0
print('Nhập số 0 để dừng chương trình và tính tổng')
while True:
	c=int(input('Nhập n: '))
	a.append(c)
	if c==0:
		a.remove(a[-1])
		for i in a:
			b+=i
		break
print('Tổng của số n là: ',b)

