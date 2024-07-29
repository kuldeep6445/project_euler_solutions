import time
import math
import functools
import operator
import itertools as it
t = time.time()

def prime(x:int):
    y = int(math.sqrt(x))+1
    if x%2==0:
        return False
    for i in range(3,y,2):
        if x%i==0:
            return False
    return True

def convertTuple(tup): 
    str = functools.reduce(operator.add, (tup)) 
    return str

def solution():
    num = '7654321'
    x = it.permutations(num,7)
    for i in x:
        if int(i[-1])%2==0:
            continue
        
        y = int(convertTuple(i))
        print(y)
        if prime(y):
            print(y)
            break   

solution()
print('time taken:',time.time()-t)