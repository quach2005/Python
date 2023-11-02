a = int(input("Nhập số a: "))
b = int(input('Nhập số b: '))
if a != 0:
	print('Phương trình đã cho có nghiệm duy nhất: \n x = -b/a')
else:
	if b==0:
		print("Phương trình có nghiệm R")
	else:
		print('Phương trình vô nghiệm')