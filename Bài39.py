a=int(input('Mời nhập sô dương a: '))
k=0
c=0
while True:
	k+=1
	c=2**k
	if c>=a:
		break
if a<0:
	print('Bạn đã Nhập sai')
elif c==a:
	print('Thuộc thuộc dạng 2^k')
else:
	print('Không thuộc dạng 2^k')
