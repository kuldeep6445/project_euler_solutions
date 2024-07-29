import time
t = time.time()

def solution():
    sum = 144
    num1 = 89
    i = 12
    while len(str(sum))<1000:
        x = sum
        sum+=num1
        num1 = x
        i+=1
    print(i)

solution()
print(time.time() - t)