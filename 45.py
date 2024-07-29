import time
t = time.time()

def check_tri(x):
    if (1+(8*x+1)**(0.5))%2==0:
        return True
    return False

def check_penta(x):
    if (1+(24*x+1)**(0.5))%6==0:
        return True
    return False

def solution():
    i=145
    while True:
        x = i*(2*i-1)
        if check_tri(x) and check_penta(x):
            print(i,x)
            break
        i+=1
print(solution())
print('time taken : ',time.time()-t)