def solution(x,y):
    x = int(x)
    y = int(y)
    count = 0
    
    while True:
        if x==1 and y==1:
            return str(count)
        elif x<=0 or y<=0 or x==y:
            return "impossible"
        else:
            if x==1 and y!=1:
                count += (y-1)
                return str(count)
            elif y==1 and x!=1:
                count += (x-1)
                return str(count)
            elif x > y:
                count += int(x/y)
                x = x%y
            elif y>x:
                count += int(y/x)
                y = y%x

print(solution('4','7'))
        