import math
a = float(input("Nhập vào số thực dương a: "))
b = float(input("Nhập vào số thực dương b: "))
c = float(input("Nhập vào số thực dương c: "))
if a+b-c>0 and b+c-a>0 and c+a-b>0:
	print("a, b, c là độ dài của tam giác")
	if a==b==c:
		print("Tam giác điều")
	elif a==b or a==c or b==c:
		print("Tam giác cân")
	elif a**2==c**2+b**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
		print("Đây là tam giác vuông")
	elif a==math.sqrt(a**2+b**2) or b==math.sqrt(a**2+c**2) or c==math.sqrt(a**2+b**2):
		print("Đây là tam giác vuông cân")
	else:
		print("Đây là tam giác thường")
else:
	print("a, b, c không phải là độ dài của tam giác")
