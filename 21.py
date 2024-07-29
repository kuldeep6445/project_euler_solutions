import time
import math
start_time = time.time()

def prime(x) ->bool:
    j=math.sqrt(x)
    for i in range(2,int(j+1)):
        if x%i==0:
            return False
    return True

div1 = [item for item in range(2,10000)]


def div_find(x:int):
    if prime(x):
        return ([[x,1]])
    else :
        log = []
        num = x
        div = div1[0]
        i = 0
        count = 0
        while True:
            if num%div==0:
                num/=div
                count+=1
            elif count!=0:
                log.append([div,count])
                count = 0
                i+=1
                div = div1[i]
            else:
                i+=1
                div = div1[i]
            if num==1:
                log.append([div,count])
                break
        return log

def div_sum(log,j):
    pro = 1
    for i in log:
        if i[0]==1:
            continue
        num = i[0]**(i[1]+1) - 1
        num /= (i[0]-1)
        pro *= num
    pro -= j
    return pro

def solution():
    num = []
    for i in div1:
        a = div_sum(div_find(i),i)
        if i == div_sum(div_find(a),a) and int(a)!=int(i):
            num.append([i,a])
    record = []
    for i in num:
        if i[0] not in record:
            record.append(i[0])
        if i[1] not in record:
            record.append(i[1])
    sum1 = 0
    for i in record:
        sum1 += i
    print(sum1)

        

solution()
print('time taken :',time.time()-start_time)