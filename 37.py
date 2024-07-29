import time
from math import sqrt
t = time.time()

def prime(x):
    if x==1:
        return False
    if x==2:
        return True
    if x%2==0:
        return False
    for i in range(3,int(sqrt(x)+1),2):
        if x%i==0:
            return False
    return True

def truncate_check(a:str):
    l = []
    for i in range(len(a)-1):
        temp = a[:(-1-i)]
        if int(temp) not in l:
            l.append(int(temp))
    for i in range(1,len(a)):
        temp = a[i:]
        if int(temp) not in l:
            l.append(int(temp))
    flag = True
    for i in l:
        if not prime(i):
            flag = False
    return flag

def solution():
    num = []
    i = 11
    while len(num)!=11:
        print(i , num)
        if truncate_check(str(i)) and prime(i):
            num.append(i)
        i += 2
    print(num)
    print(sum(num))

solution()
print('time taken : ',time.time()-t)