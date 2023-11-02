a=int(input('Nhập số a: '))
b=int(input('Nhập số b: '))
print('Bội chung của a và b là: ')
if a>b:
	for i in range(1,a+1):
		if a%i==0 and b%i==0:
			print(i,end=' ')
else:
	for i in range(1,b+1):
		if a%i==0 and b%i==0:
			print(i,end=' ')