import time
map = []

def create_map():
    f=open("67_text.txt","r")
    temp = f.readlines()
    for i in range(len(temp)):
        num = []
        for j in range(i+1):
            num.append(int(temp[i][(j*3)])*10 + int(temp[i][(j*3)+1]))
        map.append(num)
    f.close()



def solution():
    create_map()
    prev = map[-1]
    for i in range(len(map)-2,0-1,-1):
        temp = []
        for j in range(len(map[i])):
            if prev[j]>=prev[j+1]:
                temp.append(map[i][j]+prev[j])
            else:
                temp.append(map[i][j]+prev[j+1])
        
        prev = temp
    print(prev)
 
t = time.time()
solution()
print("time taken :",time.time()-t)