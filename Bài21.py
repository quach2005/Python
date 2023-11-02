a=float(input("Nhập điểm Toán: "))
b=float(input('Nhập điểm Văn: '))
c=float(input('Nhập điểm Anh: '))
t= (a+b+c)/3
print('Điểm tổng: ',t)
if t>=8 and a>=8 or b>=8 and a==b==c>6.5:
	print('Học Sinh Giỏi')
elif t>=6.5 and a>=6.5 or b>=6.5 and a==b==c>5:
	print('Học Sinh Khá')
elif t>=5 and a>=5 or b>=5 and a==b==c>5:
	print('Học Sinh Trung Bình')
elif t>=3.5 and a>=5 or b>=3.5 and a==b==c>2:
	print('Học Sinh Yếu')
elif t<3.5:
	print('Học Sinh Kém')
else:
	print('Bạn Nhập Sai')
