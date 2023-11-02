
n=int(input("Nhập tháng: "))

if n in [1,3,5,6,8,10,12]:
	print("Tháng",n,"có 31 ngày")
elif n in [4,7,9,11]:
	print("Tháng",n,"có 30 ngày")
else:
	print("Tháng",n,"có 28 ngày")