def C_language_bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(1, len(lst) - i):
            if lst[j] < lst[j-1]:
                temp = lst[j]
                lst[j] = lst[j-1]
                lst[j-1] = temp

def bubble_sort(lst):
    top = len(lst) - 1
    is_exchanged = True

    while is_exchanged:
        is_exchanged = False
        for i in range(top):
            if lst[i] > lst[i + 1]:
                is_exchanged = True
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
        top -= 1

lst = [1, 5, 0, 6, 10, 16, 54, 3]
bubble_sort(lst)
print lst
