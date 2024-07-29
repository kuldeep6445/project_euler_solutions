import time
from math import sqrt
t = time.time()

def prime(x:int):
    if x==2:
        return True
    if x%2==0:
        return False
    for i in range(3,int(sqrt(x)+1),2):
        if x%i==0:
            return False
    return True

p_list = [i for i in range(2,100000) if prime(i)]


def factorize(num:int):
    l = []
    count = 0
    a = 0
    while num != 1:
        if num%p_list[a]==0:
            num /= p_list[a]
            count += 1
        else:
            if count!=0:
                l.append([p_list[a],count])
            a+=1
            count = 0
        if num==1:
            l.append([p_list[a],count])
    return l

def check(a,b,c,d):
    for i in a:
        if i in b or i in c or i in d:
            return False
    for i in b:
        if i in c or i in d:
            return False
    for i in c:
        if i in d:
            return False
    return True


def solution():
    i = 8
    a = factorize(8)
    b = factorize(9)
    c = factorize(10)
    d = factorize(11)
    while True:
        

        if check(a,b,c,d) :
            return i
        a = b
        b = c
        c = d
        d = factorize(i+4)
        i+=1
print(solution())

print('time taken : ',time.time()-t)