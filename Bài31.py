a=int(input('Nhập số a: '))
def ktra(a):
	if a >3:
		for i in range(2,a-1):
			if a%i==0:
				kq='Đây không phải là số nguyên tố'
			elif a%i==1:
				kq='Đây là số nguyên tố'
	elif a<=3 and a>1:
		kq='Đây là số nguyên tố'
	else:
		kq='Đây không phải là số nguyên tố'

	return kq
print(ktra(a))