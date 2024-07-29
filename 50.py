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


#78497
def solution():
    l = []
    sum = 0
    for i in range(2,1000000):
        if prime(i):
            sum+=i
            l.append([i,sum])
    print('step 1 complete')
    num = []
    for i in range(len(l)-1,0-1,-1):
        for j in range(len(l)):
            if l[i][0] - l[j][1]<=0:
                break
            elif prime(l[i][0] - l[j][1]):
                num.append([l[i][0],i,j,i-j])
            if len(num)==10:
                print(num)
                return
    print(num)



solution()
print('time taken : ',time.time()-t)
