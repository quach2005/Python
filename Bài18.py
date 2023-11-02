a = int(input("Nhập số a: "))
b= int(input('Nhập số b: '))
c= int(input('Nhập số c: '))
d= b**2-4*a*c
if a==0:
	if b==0:
		print('Phương trình có nghiệm R')
	else:
		print('Phương trình vô nghiệm')
elif d>0:
	print('Phương trình có 2 nghiệm phân biệt')
elif d==0:
	print('Phương trình có 1 nghiệm kép: x= -b/2a')
else:
	print("Phương trình vô nghiệm")