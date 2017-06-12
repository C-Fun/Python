def bi_search(lst, x):
    lst.sort()
    print lst
    low = 0
    high = len(lst) - 1
    while(low <= high):
        mid = (low + high) / 2
        if(lst[mid] < x):
            low = mid + 1
        elif(mid > x):
            high = mid - 1
        else:
            return mid
    return False

a = 1
lst = []
while(a):
    a = int(raw_input("Input a('0' to end):"))
    if(a):
        lst.append(a)

x = int(raw_input("Input x:"))

print bi_search(lst, x)
