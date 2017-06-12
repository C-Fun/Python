# -*- coding: cp936 -*-
###使用列表解析对所输入数字x的因数求和###
'''
x = int(raw_input())
print sum([i for i in range(1, x+1)if x%i == 0])'''


###按照成绩从高到低排序###

students = [['Zhang', 84],
            ['Wang', 77],
            ['Li', 100],
            ['Zhao', 53]]
'''
def f(a):
    return a[1]

students.sort(key = students[1], reverse = True)
'''
###匿名函数###

students.sort(key = lambda x: x[1], reverse = True)

print students
