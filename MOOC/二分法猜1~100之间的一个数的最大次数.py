count = 0
for i in range(1, 101):
    cnt = 0
    left = 1
    right = 101
    mid = 0
    while left < right:
        cnt += 1
        mid = int((left + right) / 2)
        if i < mid:
           right = mid
        elif i > mid:
            left = mid
        else:
            break
    if cnt > count:
        count = cnt
print count
        
