import time as tt
t = tt.time()

def solution():
    num = '1'
    next = 2
    for i in range(1,1000000):
        if i == len(num):
            num += str(next)
            next += 1
    x = 1
    for i in range(7):
        x *= int(num[10**i -1])
    print(x)
    

solution()
print("time taken: ",tt.time()-t)