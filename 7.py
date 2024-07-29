import ksb


count =0
i=1

while count!=10001:
    i+=1
    if ksb.prime(i):
        count+=1
        j=i
        print(f"{j}  {count}")
       

