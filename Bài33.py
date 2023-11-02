n = int(input('Nhập số n: '))
c = 0
def kq(n,c):
	while True:
		for i in range(1,n+1):
			c+=i
			if c<n:
				kq=i
		return kq
print(kq(n,c))
