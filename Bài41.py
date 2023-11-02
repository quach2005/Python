n=input('Nhập chuỗi: ')
def ktr(n):
      dem=0
      for i in n.split():
            dem+=1
      return dem
print('Có',ktr(n),'trong chuỗi này')