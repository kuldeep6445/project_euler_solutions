import time
start = time.time()
fact = [1,1,2,6,24,120,720,5040,40320,362880]
def solution():
    num = []
    for i in range(3,1000000):
        sum = 0
        x = str(i)
        for j in x:
            sum += fact[int(j)]
        if sum == i:
            num.append(i)
    print(num)
    print(num[0]+num[1])

solution()


print("time taken : ",time.time()-start)