import ksb


num = 3
add = 3
check = 0
while check<=500:
    check = ksb.checkdiv(num)
    print(num,"\t",check)
    num+=add
    add+=1

