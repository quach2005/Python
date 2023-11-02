# b=input('Nhập mật khẩu của bạn: ')
a='~,!,@,#,$,%,^,&,*,(,),_,+,-'
a.split(',')
c='0,1,2,3,4,5,6,7,8,9'
c.split(',')
d=0
while True:
    b=input('Nhập mật khẩu của bạn(Bao gồm ký tự đặc biệt, số, chữ hoa và thường: ')
    for i in b:
        if i.islower():
            for i in b:
                if i.isupper():
                    for i in b:
                        for j in a:
                            if i==j:
                                for i in b:
                                    for j in c:
                                        if i==j:
                                            d=b
    if d!=0 and len(d)>=6:
        print('*---------------------*\n')
        print('Mật Khẩu Của Bạn Là: ',d,'\n')
        print('*---------------------*\n')
        break
    else:
        print('*---------------------*\n')
        print('Mật Khẩu Của Bạn Quá Kem \n*---------------------*\nMời Bạn Nhập Lại\n')
                