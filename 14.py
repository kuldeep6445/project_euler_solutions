import time
start_time = time.time()
record = {}
def solve(x:int):
    y = x
    temp = []
    while x!=1:
        if record.get(x)!=None:
            return len(temp)+record.get(x)
        x = move(x)
        temp.append(x)
    return len(temp)+1

def move(x:int)->int:
    if x%2==0:
        return x/2
    elif x==1:
        return 1
    else:
        return (3*x +1)

def solution():
    max = 1
    num = 1
    for i in range(2,1000000):
        y = solve(i)
        record.update({i:y})
        if y>max:
            max = y
            num = i
    print(max,num)  
        


solution()

print('time taken : ',time.time()-start_time)