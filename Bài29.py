a= int(input('Nhập số a: '))
def kq(a):
	dem=0
	for i in range(1,a+1):
		if a%i==0:
			dem=dem+1

	return dem
print('Số ước của a là:',kq(a))