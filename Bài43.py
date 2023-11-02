a=input('Nhập 3 số nguyên: ')
a=a.split(',')
b=0
for i in (a[0],a[1],a[2]):
	b+=int(i)
	
print('Tổng của 3 số là: ',b)