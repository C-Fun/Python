import math
n = input()
count = 1
for i in range(3, n, 2):
    for h in range(2, int(math.sqrt(i))+1):
        if i % h == 0:
            break
    else:
        num = i
        cnt = 0
        while num != 0:
            num /= 10
            cnt += 1
            p = cnt - 1
        num = i
        flag = 1
        while cnt and flag:
            cnt -= 1
            for j in range(2, int(math.sqrt(num))+1):
               if num % j == 0:
                    flag = 0
                    break
            a = num % 10
            num /= 10
            num = a*(10**p) + num        
        if flag:
            count += 1
print count
