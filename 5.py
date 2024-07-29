def prime(x:int) ->bool:
    
    for i in range(2,x):
        if x%i==0:
            return False
    return True

num =1

for i in range(2,21):
    if prime(i):
        num *= i
    else:
        j = i
        for k in range(2,i):
            if j%k==0:
                j = j/k
        num *=j

print(num)

