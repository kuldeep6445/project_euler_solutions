import time
from math import sqrt
t= time.time()

def prime(x):
    if x%2==0:
        return False
    for i in range(3,int(sqrt(x)+1),2):
        if x%i==0:
            return False
    return True

def check(x):
    for i in x:
        if int(i)%2==0:
            return False
    return True

def rotate(a):
    l = []
    b = str(a)
    for i in range(len(b)):
        temp = b[:-1]
        c = b[-1]
        c += temp
        b = c
        l.append(int(b))
    return l

def solution():
    num = []
    for i in range(1000000):
        if check(str(i)):
            l = rotate(i)
            flag = True
            for j in l:
                if not prime(j):
                    flag = False
            if flag :
                num.append(i)
    print(num)
    print(len(num))
solution()
print(time.time()-t)