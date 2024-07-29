l = [ 200 , 100 , 50 , 20 , 10 , 5 , 2 , 1 ]


l = [1,2,5,10,20,50,100,200]

ways = [0]*201
ways[0] = 1
for i in range(len(l)):
    for j in range(l[i],201):
        ways[j] += ways[j - l[i]]
print(ways[200])