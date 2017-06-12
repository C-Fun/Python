def change_sort(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j] < lst[i]:
                temp = lst[j]
                lst[j] = lst[i]
                lst[i] = temp

lst = [10, 5, 8, 13, 50, 161, 0, 1, 16]
change_sort(lst)
print lst
