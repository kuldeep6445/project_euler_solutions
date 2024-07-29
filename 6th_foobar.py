import time
mylist1 = []
for i in range(1,2000):
    mylist1.append(i)
y = time.time()
def find_greater(l,pointer):
    item = []
    for i in l[:pointer]:
        if l[pointer]%i==0:
            item.append(i)
    return len(item)
def find_lesser(l,pointer):
    item = []
    for i in l[pointer+1:]:
            if i%l[pointer]==0:
                item.append(i)
    return len(item)
    
def solution(l):
    pointer = len(l) -2
    count = 0
    while pointer>0:
        count+=(find_greater(l,pointer) * find_lesser(l,pointer))
        pointer-=1
    return count
                 


print(solution(mylist1))
print(time.time()- y)
        