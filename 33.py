import time
import fractions as fr
t= time.time()

num = []
def check(i,j):
    i = str(i)
    j = str(j)
    fr1 = fr.Fraction(1,1)
    if i[1]=='0'and j[1]=='0':
        return
    if i[1]==j[1] and j[0]!='0':
        fr1 = fr.Fraction(int(i[0]),int(j[0]))
    elif i[1]==j[0] and j[1]!='0':
        fr1 = fr.Fraction(int(i[0]),int(j[1]))
    elif i[0]==j[1] and j[0]!='0':
        fr1 = fr.Fraction(int(i[1]),int(j[0]))
    elif i[0]==j[0] and j[1]!='0':
        fr1 = fr.Fraction(int(i[1]),int(j[1]))
    fr2 = fr.Fraction(int(i),int(j))
    if fr1 == fr2:
        num.append(fr2)

def solution():
    for i in range(10,100):
        for j in range(i+1,100):
            check(i,j)
    pro = 1
    for i in num:
        pro *= i
    print(num)
    print(pro)
    
solution()

print(time.time()-t)