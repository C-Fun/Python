def search(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    else:
        return 0

lst = (10, 5, 8, 13)

print search(lst, 7)
