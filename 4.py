
def pallin(num:int)->bool:
    if num>=100000 and num<=999999 :
        strnum = str(num)
        if strnum[0]==strnum[5] and strnum[1]==strnum[4] and strnum[2]==strnum[3]:
            return True
    elif num<=99999 and num>1000:
        strnum = str(num)      
        if strnum[0]==strnum[4] and strnum[1]==strnum[3]:
            return True
    return False

track =0

for i in range(100,1000):
    for j in range(100,1000):
        if pallin(i*j):
            if i*j > track:
                track = i*j

print(track)