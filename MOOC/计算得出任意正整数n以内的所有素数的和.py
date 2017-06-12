import math
n = input()
sum = 0
for i in range(2, n):
    flag = 1
    for j in range(2,int(math.sqrt(i)+1)):
        if i % j ==0:
            flag = 0
    if flag:
        sum += i
print sum
