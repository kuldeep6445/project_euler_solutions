import time
t = time.time()

num = 1
sum = 1
add = 2
for i in range(1,501):  
    for j in range(4):
        num+=add
        sum+=num   
    add+=2
    
print(sum)
print("time taken : ",time.time()-t)