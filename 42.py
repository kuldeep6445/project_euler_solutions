import time
t = time.time()
num = []
def creator():
    for i in range(150):
        x = i*(i+1)/2
        num.append(x)

def solution():
    creator()
    f = open('words.txt','r')
    str = f.readline()
    reading = False
    total = 0
    count = 0
    for i in range(len(str)):

        if reading and str[i]!='"':
            count += (ord(str[i])-64)

        if str[i]=='"':
            if reading :
                if count in num:
                    total +=1
                count = 0
                reading = False
            else :
                reading = True
    print(total)       
            
            


solution()
print('time taken : ',time.time()-t)