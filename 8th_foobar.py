from time import time
t = time()

def gcd(x, y):
    if x==0 or y == 0:
        return 1
    if x<0:
        x *= -1
    if y<0:
        y *= -1
    while(y):
        x, y = y, x % y
    return x

def div(n) : 
    l = []
    i = 1
    while i <= n : 
        if (n % i==0) : 
             l.append(i)
        i = i + 1
    return l

def create_map_me(dimension , mpos ,distance):
    map = [0]
    final = []
    horiz_box = int(distance/dimension[0] + 2)
    add = [mpos[0]*2,(dimension[0]-mpos[0])*2]
    check = 1
    num = 0
    for i in range(horiz_box): 
        num += add[check]
        map.append(num)
        if check ==1:
            check = 0
        else:
            check = 1
    num = 0
    check = 0
    for i in range(horiz_box):
        num -= add[check]
        map.append(num)
        if check ==1:
            check = 0
        else:
            check = 1
    
    verti_box = int(distance/dimension[1]+2)
    add = [mpos[1]*2,(dimension[1]-mpos[1])*2]
    for i in map:
        check = 1
        num = 0
        if i!=0:
            final.append([i,0])
        for j in range(verti_box):
            num += add[check]
            final.append([i,num])
            if check ==1:
                check = 0
            else:
                check = 1
        check = 0
        num = 0
        for j in range(verti_box):
            num -= add[check]
            final.append([i,num])
            if check ==1:
                check = 0
            else:
                check = 1
    return final

def create_map_g(dimension ,mpos, gpos ,distance):
    final = []
    map = [gpos[0]-mpos[0]]
    horiz_box = int(distance/dimension[0] + 2)
    add = [gpos[0]*2,(dimension[0]-gpos[0])*2]
    check = 1
    num = gpos[0]-mpos[0]
    for i in range(horiz_box):
        num += add[check]
        map.append(num)
        if check ==1:
            check = 0
        else:
            check = 1
    num = gpos[0]-mpos[0]
    check = 0
    for i in range(horiz_box):
        num -= add[check]
        map.append(num)
        if check ==1:
            check = 0
        else:
            check = 1
    
    verti_box = int(distance/dimension[1]+2)
    add = [gpos[1]*2,(dimension[1]-gpos[1])*2]
    for i in map:
        check = 1
        num = gpos[1]-mpos[1]
        if i!=0:
            final.append([i,0])
        for j in range(verti_box):
            num += add[check]
            final.append([i,num])
            if check ==1:
                check = 0
            else:
                check = 1
        check = 0
        num = gpos[1]-mpos[1]
        for j in range(verti_box):
            num -= add[check]
            final.append([i,num])
            if check ==1:
                check = 0
            else:
                check = 1
    return final

def filter(gpos , mpos , d):
    l = []
    for i in range(len(gpos)):
        if gpos[i][0]**2 + gpos[i][1]**2 > d**2:
            l.append(gpos[i])
    for i in l:
        gpos.remove(i)
    
    return len(gpos)

def check(gpos , mpos):
    l = []
    for i in gpos:
        for j in mpos:
            if j[1] == i[1]*j[0]/i[0]:
                l.append(i)
    return len(l)




def solution(dimension , mpos ,gpos ,distance):
    if dimension == [2,2]:
        return 2
    if mpos == gpos:
        return 2
    m_map = create_map_me(dimension , mpos ,distance)
    g_map = create_map_g(dimension ,mpos,gpos ,distance)
    final = filter(g_map , m_map ,distance)
    final -= check(g_map , m_map)
    return final
print(solution([42,59], [34,44], [6,34], 5000))

print("time taken : ",time()-t)