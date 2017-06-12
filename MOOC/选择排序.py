def selection_sort(lst):
    for i in range(len(lst) - 1):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst.insert(i, lst.pop(min_idx))

lst = [0, 565, 16, 8, 1, 16, 261]
selection_sort(lst)
print lst
