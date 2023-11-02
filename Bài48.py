# Nhập và ép kểu
nember = int(input("Nhập số n: "))
nember = " "+str(nember)
# Xử lý chuỗi
so = ""
for i in range(len(nember)):
    so+=nember[i]
    if i%3==0 and i!=0:
        so+="."
# Xoá dấu (.) cuối dòng
if i%3==0:
    so=so[:-1]
print(so)