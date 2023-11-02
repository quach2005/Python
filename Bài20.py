thg=int(input("Nhập ngày: "))
m=int(input("Nhập tháng: "))
th1=31
th2=28
th4=30
def thang(thg,m):

	if m==1:
		kq=thg
	elif m==2:
		kq=th1+thg
	elif m==3:
		kq=th1+th2+thg
	elif m==4:
		kq==th1*2+th2+thg
	elif m==5:
		kq=th1*2+th2+th4+thg
	elif m==6:
		kq=th1*3+th2+th4+thg
	elif m==7:
		kq=th1*4+th2+th4+thg
	elif m==8:
		kq=th1*4+th2+th4*2+thg
	elif m ==9:
		kq=th1*5+th2+th4*2+thg
	elif m==10:
		kq=th1*5+th2+th4*3+thg
	elif m==11:
		kq=th1*6+th2+th4*3+thg
	elif m==12:
		kq=th1*6+th2+th4*4+thg
	return kq
print("Ngày",thg,"Tháng",m,"Cách Ngày Đầu Năm",thang(thg,m),"Ngày")