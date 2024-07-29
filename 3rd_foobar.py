
def maximum(lambs):
    money = lambs -2
    max_list = [1,1]
    j=2
    while True:
        if money - (max_list[j-1]+max_list[j-2])>=0:
            max_list.append(max_list[j-1]+max_list[j-2])
            money -= max_list[j-1]
            money -= max_list[j-2]
            j+=1
        else:
            return len(max_list)

def minimum(lambs):
    money = lambs - 3
    min_list = [1,2]
    j=2
    while True:
        if money - (min_list[j-1]*2)>=0:
            min_list.append(2*min_list[j-1])
            money -= min_list[j-1]*2
            j+=1
        else:
            #if money>= min_list[j-1]+min_list[j-2] and money<=min_list[j-1]*2:
             #   min_list.append(money)
            #sum1=0
            #for i in min_list:
            #    sum1+=i
            #print(sum1)
            return len(min_list)
  
    



def solution(total_lambs):
    if total_lambs==2 or total_lambs==1 or total_lambs==0:
        return 0
    else:
        return (maximum(total_lambs)-minimum(total_lambs)

f = open("mydata.txt","w")

for i in range(10,10000):
    f.write(maximum(i),' - ',minimum(i),' = ',maximum(i)-minimum(i),"\n")
