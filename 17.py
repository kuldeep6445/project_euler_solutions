#         0,1,2,3,4,5,6,7,8,9
first  = [0,3,3,5,4,4,3,5,5,4]
second = [0,0,6,6,6,5,5,7,6,6]

def underhund(x:int)->int:
    if x==0:
        return 0
    elif x<=19 and x>=10:
        if x==10:
            return 3
        elif x==11:
            return 6
        elif x==12:
            return 6
        elif x==13:
            return 8
        elif x==14:
            return 8
        elif x==15:
            return 7
        elif x==16:
            return 7
        elif x==17:
            return 9
        elif x==18:
            return 8
        elif x==19:
            return 8
    else:
        b = int(x/10)
        c = int(x%10)
        return (first[c]+second[b])

def hund(x:int)->int:
    if x==0:
        return 0
    else:
        return(first[x]+8)

sum =11
for i in range(1,1000):
    a=int(i/100)
    b=int(i%100)
    sum += (hund(a) + underhund(b))
    if a!=0 and b!=0:
        sum +=3
print(sum)
