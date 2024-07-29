
def solution():
    total = 0
    for i in range(2,500000):
        num = str(i)
        sum = 0
        for j in num:
            sum += (int(j)**5)
        if sum == i:
            total+=i
    print(total)

solution()
        