# -*- coding: cp936 -*-
"""C语言函数法
def aver(lst):
    Sum = 0
    for i in range(len(lst)):
        Sum += lst[i][1]
    return float(Sum) / len(lst)

students = [['Zhang', 84],
            ['Wang', 77],
            ['Li', 100],
            ['Zhao', 53]]

print aver(students)
"""
###列表解析法###

students = [['Zhang', 84],
            ['Wang', 77],
            ['Li', 100],
            ['Zhao', 53]]

print float(sum([x[1] for x in students])) / len(students)
