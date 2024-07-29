import time
from math import sqrt
t = time.time()

def prime(num):
    if num==2:
        return True
    if num%2==0:
        return False
    for i in range(3,sqrt(num)+1,2):
        if num%i==0:
            return False
    return True

def permutations(arr):
    if len(arr)==0:
        return []
    elif len(arr)==1:
        return [arr]
    l = []
    for i in range(len(arr)):
        x = arr[i]
        newlist = arr[:i] + arr[i+1:]
        for p in permutations(newlist):
            if ([x]+p) not in l:
                l.append([x]+p)
    return l

def get_pattern():
    final = []
    l = ['y','y','y']
    for i in range(1,4):
        l.append('x')
        final.extend(permutations(l))
    return final

def solution():
    l = get_pattern()
    for i in l:
        



print('time taken : ',time.time()-t)