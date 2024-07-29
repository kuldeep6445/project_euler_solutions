import time
t= time.time()




def solution():
    num = set('123456789')

    final = set()
    for i in range(2,60):
        for j in range(123,10000) :
            x = i*j
            
            l = str(i)+str(j)+str(x)
            if len(l)==9 and set(l)==num:
                final.add(x)
                if x==6952:
                    print(i,j)

    print(final)
    print("sum : ",sum(final))
    
        
            

solution()

print("time taken : ",time.time()-t)