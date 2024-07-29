month = [31,28,31,30,31,30,31,31,30,31,30,31]

def leap(x:int)->int:
    if x%400==0:
        return 29
    elif x%100==0:
        return 28
    elif x%4==0:
        return 29
    else:
        return 28

def solution():
    sum = 0
    cache = 2
    for i in range(1901,2001):
        print('\n')
        for j in range(12):
            print(cache,end=" ")
            if cache==0:
                sum+=1
            if j==1:
                cache += leap(i)
                cache = cache%7
            else:
                cache += month[j]
                cache = cache%7
    print('\n\n\n',sum)
solution()