#Nhập dữ liệu
print('\n')
a = int(input('Nhập số A: '))
b=1
c=1


#sử lí vòng lập
while c+b<a:
	b+=c

	c+=b

print('\n')
print('*-----------------*')
print('\n')
#điều kiện và in ra kết quả
if b>a>c:
	print('Số lớn nhất trong dãy số fibonacci nhỏ hơn A là:',c)
elif c>a>b:
	print('Số lớn nhất trong dãy số fibonacci nhỏ hơn A là:',b)
else:
	print('Số lớn nhất trong dãy số fibonacci nhỏ hơn A là:',max(b,c))

print('\n')
# print(b,'\n')
# print(c,'\n')