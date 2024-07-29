def find(x)->int:
    num = []
    r = 1
    for i in range(3000):
        
        r *= 10
        if x > r:
            r*=10
        if x > r:
            r*=10
        if x > r:
            r*=10
        if x > r:
            r*=10
        if x > r:
            r*=10
        a = divmod(r,x)
        num.append(a[0])
        r = a[1]
        if r==0:
            break
    if len(num)<2998:
        return 0
    a = [num[2999]]
    for i in range(len(num)-2,0-1,-1):
        if num[i] == a[0]:
            check = 0
            for j in range(len(a)):
                if num[i-j]==a[j]:
                    check+=1
            if check == len(a):
                return check     
        a.append(num[i])
        
        

def solution():
    num = 0
    val = 0
    for i in range(3,1000):
        print(i)
        if val < find(i):
            val = find(i)
            num = i
    print(num,val)
solution()
