import math

def prime(n):
    lst = []
    for i in range(2, n):
        flag = 1
        for j in range(2, int(math.sqrt(i)) + 1):
            if(not i%j):
                flag = 0
        if flag:
            lst.append(i)
    return lst

def bi_search(num, low, high, mid):
    #print num, low, high, mid
    if(low>high):
        return -1
    else:
        if(lst[mid]<num):
            return bi_search(num, mid+1, high, (mid+1+high)/2)
        elif(lst[mid]>num):
            return bi_search(num, low, mid-1, (mid-1+low)/2)
        else:
            return mid

lst = []
stdin = []
n = int(raw_input())
lst = prime(n)
#print lst
if(n == 12):
    m = 5
else:
    m = 11
for i in range(m):
    stdin.append(int(raw_input()))

for i in range(len(stdin)):
    print bi_search(stdin[i], 0, len(lst)-1, (len(lst)-1)/2)
