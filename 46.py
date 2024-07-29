import time
from math import sqrt
t = time.time()

def prime(x:int):
    if x%2==0:
        return False
    for i in range(3,int(sqrt(x)+1),2):
        if x%i==0:
            return False
    return True

p_list = [i for i in range(3,10000) if prime(i)]

def next(i):
    while True:
        i+=2
        if (not prime(i)):
            return i

def solve(num):
    a = 0
    b = 0
    
    while num>p_list[a]:
        while True:
            if num - (p_list[a] + 2*(b**2))==0:
                #print(num,' = ',p_list[a],' + 2*(',b,'** 2)')
                return True
            elif num - (p_list[a] + 2*(b**2))>0:
                b+=1
            else:
                break
        a += 1
        b = 0
    return False

#5777

def solution():
    i = 5
    while True:
        if not solve(i):
            return i
        i = next(i)
print(solution())

print('time taken : ',time.time()-t)