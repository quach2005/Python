a=input('Nhập một chuỗi: ')
b=0
for i in a:
	if not i.isupper() and not i.islower():
		if i != ' ' and i!=',' and i!='.':

			for j in i:
				b+=int(j)
print('Tổng là: ',b)