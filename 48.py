import time
t = time.time()

def carry(num):
    for i in range(len(num)-1,0,-1):
        if num[i] >=10:
            num[i-1] += int(num[i]/10)
            num[i] = num[i]%10
    return num

def add(num , x):
    for i in range(0,len(x)):
        num[-1-i] += int(x[-1-i])
    num = carry(num)
    return num

def solution():
    num = [0 for i in range(3000)]
    num.insert(0,1)
    for i in range(1000,0,-1):
        add(num,str(i**i))
    print(num)
    
solution()
print('time taken : ',time.time()-t)