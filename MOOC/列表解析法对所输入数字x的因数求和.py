# -*- coding: cp936 -*-
###ʹ���б����������������x���������###
'''
x = int(raw_input())
print sum([i for i in range(1, x+1)if x%i == 0])'''


###���ճɼ��Ӹߵ�������###

students = [['Zhang', 84],
            ['Wang', 77],
            ['Li', 100],
            ['Zhao', 53]]
'''
def f(a):
    return a[1]

students.sort(key = students[1], reverse = True)
'''
###��������###

students.sort(key = lambda x: x[1], reverse = True)

print students
