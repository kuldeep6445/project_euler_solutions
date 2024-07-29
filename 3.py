num = 600851475143

def prime(x:int) ->bool:
    
    for i in range(2,x):
        if x%i==0:
            return False
    return True

i=2
while num!=1:
    if prime(i) and num%i==0:
        buffer = i
        num = num/i
        i=2

    i+=1
print(buffer)
