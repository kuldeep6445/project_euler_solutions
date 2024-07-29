def carry(num):
    for i in range(len(num)-1,0,-1):
        if num[i]>9:
            num[i-1] += int(num[i]/10)
            num[i] = num[i]%10
    return num

def add(num,buffer):
    for i in range(50):
        num[i] += int(buffer[i])
    num = carry(num)
    return num

def solution():
    f = open('13text.txt','r')
    num = [0 for i in range(50)]
    for i in range(100):
        buffer = f.readline()
        buffer = buffer[0:-1]
        num = add(num,buffer)
    return num
for i in solution():
    print(i,end='')
#print(carry([1,2,3,40,90]))