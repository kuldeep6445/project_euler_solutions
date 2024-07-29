num1 = 1
num2 = 2
sum = 2

while num2<4000000 :
    temp = num1
    num1 = num2
    num2 += temp
    if num2%2==0 and num2<4000000:
        sum += num2

print(sum)