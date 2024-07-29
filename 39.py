import time
t = time.time()


def solution():
    num = []
    for i in range(1,1000):
        for j in range(i,1000):
            h = (i**2+j**2)**(1/2)
            if h.is_integer():
                num.append(i+j+h)
    num.sort()
    print(num)
    l = []
    a = num[0]
    count = 1
    for i in num[1:]:
        if i==a:
            count +=1
        else:
            l.append([a,count])
            a = i
            count = 1
    max1 = 0
    p = 0
    for i in l:
        if i[1] > max1 and i[0]<1001:
            max1 = i[1]
            p = i[0]
    print(p,max1)



        
                





solution()

print('time taken : ',time.time()-t)