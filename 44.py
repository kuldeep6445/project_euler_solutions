import time
t = time.time()

def extend(num,i):
    index = len(num)
    while num[-1] < num[i] + num[i-1]:
        num.append(int(index*(index*3 - 1)/2))
        index += 1
    return num

def find(a):
    if int(1+(24*a+1)**(0.5))%6==0:
        return True
    return False
#5482660

def solution():
    num = [0,1,5,12]
    i = 2
    while True:
        if num[-1] < num[i] + num[i-1]:
            num = extend(num,i)
        for j in range(1,i):
            if num[i]+num[j] in num[i:] and find(num[i]-num[j]): 
                return([[num[j],num[i]],[j,i]])    
        i+=1
print(solution())

print('time taken : ',time.time()-t)