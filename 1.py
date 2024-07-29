
sum =8

for i in range(6,1000):
    
    if i%3==0:
        sum+=i
    if i%5==0:
        sum+=i
    if i%15==0:
        sum-=i        
    

print(sum)