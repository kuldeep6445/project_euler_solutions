import time
import math
t = time.time()

def divSum(num) : 
    y = num
    # Final result of summation of divisors 
    result = 0
      
    # find all divisors which divides 'num' 
    i = 2
    while i<= (math.sqrt(num)) : 
        
        # if 'i' is divisor of 'num' 
        if (num % i == 0) : 
        
            # if both divisors are same then 
            # add it only once else add both 
            if (i == (num / i)) : 
                result = result + i; 
            else : 
                result = result +  (i + num/i); 
        i = i + 1

    if y> (result + 1):
        return True
    return False

def check_abundant(num):
    y = num
    i = 2
    count = 0
    l = []
    while num!=1:
        if num%i==0:
            num /= i
            count += 1
        else:
            if count!=0:
                l.append([i,count])
            i += 1
            count = 0
        if num==1:
            l.append([i,count])
    pro = 1
    for i in l:
        pro *= (i[0]**(i[1]+1)-1)/(i[0]-1)
    pro -= y
    if y<pro:
        return True
    return False

def solution():
    ablist = []
    for i in range(12,28124):
        print(i)
        if divSum(i):
            ablist.append(i)
    print(ablist)
solution()
print('time taken : ',time.time()-t)