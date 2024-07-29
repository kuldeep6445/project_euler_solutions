fact = [1,1,2,6,24,120,720,5040,40320,362880]

def create(l):
    num = [0,1,2,3,4,5,6,7,8,9]
    result = []
    for i in l:
        result.append(num[i])
        num.pop(i)
    
    for i in result:
        print(i,end="")
    print(" ",end="")
    for i in num:
        print(i,end="")

def solution(x:int):
    num = []
    sum = x
    i = 9
    count = 0
    while sum>0:
        if sum - fact[i]>=0:
            count += 1
            sum -= fact[i]
        else:
            num.append(count)
            count = 0
            i-=1
    print(num)
    return create(num) 
    
solution(1000000)
