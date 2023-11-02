nhap=input('Nhập vào một chuỗi: ')
upper=lower=so=0
for i in nhap:
	if i.isupper():
		upper+=1
	if i.islower():
		lower+=1
	if i ==' 'and','and '.'and ':':
		continue
	if not i.islower() and not i.isupper():
		so+=1
print('Só kí tự in hoa là: ',upper)
print('Số kí tự in thường là: ',lower)
print('Số ký tự số là: ',so)