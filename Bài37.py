a=[]
b=[]
c=[]
d=[]
while True:
	b=int(input("Nhập số nguyên dương n: "))
	a.append(b)
	if b<0:
		a.remove(a[-1])
		for i in a:
			if i%2==0:
				c.append(i)
			if i%2!=0:
				d.append(i)
		break
print('Có',len(set(c)),'Số Chẵn')
print('Có',len(set(d)),'Số lẻ')