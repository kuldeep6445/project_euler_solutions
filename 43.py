import itertools
import time
t = time.time()


def solution():
    num = '0123456789'
    sum = 0
    x = itertools.permutations(num)
    l = []#1430952867 + 1460357289 + 1406357289 + 4130952867 + 4160357289 + 4106357289
    for i in x:
        if (int(''.join(i[1:4]))%2==0 and
           int(''.join(i[2:5]))%3==0 and
           int(''.join(i[3:6]))%5==0 and
           int(''.join(i[4:7]))%7==0 and
           int(''.join(i[5:8]))%11==0 and
           int(''.join(i[6:9]))%13==0 and
           int(''.join(i[7:10]))%17==0):
           sum += int(''.join(i))
           l.append(int(''.join(i)))

    print(sum)
    print(l)
solution()

print('time taken : ',time.time()-t)