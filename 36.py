import time
t = time.time()

def number_creator(x:int):
    num = []
    a = str(x)
    size = len(a)
    if size==1:
        num.append(x)
    if size==2:
        temp = ''
        temp += a[1] + a[0] + a[1]
        num.append(int(temp))
    elif size==3:
        temp = ''
        temp += a[2]+a[1]+a[0]+a[1]+a[2]
        num.append(int(temp))
    for i in range(7-size*2):
        l = ''
        for j in range(len(a)-1,0-1,-1):
            l += a[j]
        for j in range(0,i):
            l += '0'
        l += a
        num.append(int(l))
    
    return num

def convertor(x:int):
    if x==0:
        return '0'
    num = ''
    while x!=1:
        x,r = divmod(x,2)
        num =  str(r) + num
    num = '1' + num
    return num

def pall_check(x:str):
    size = len(x)
    for i in range(int(size/2)):
        if x[i] != x[0-(i+1)]:
            return False
    return True
    

def solution():
    num = []
    for i in range(1,1000):
        if i%10==0:
            continue
        l = number_creator(i)
        for j in l:
            binr = convertor(j)
            if pall_check(binr):
                num.append(j)
    print(num)
    print("length: ",len(num))
    print("sum: ",sum(num))
solution()

print("time taken : ",time.time()-t)