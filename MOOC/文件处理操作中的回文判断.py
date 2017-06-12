# -*- coding: cp936 -*-

f = open(r'D:\大学课程学习资料\Python\names.txt', 'r')

def judge(name):
    low = 0
    high = len(name)-1
    while low <= high :
        if not name[low] == name[high] :
            return False
        else:
            low += 1
            high -= 1
    return True

lenth = 0
flag = ''

for line in f:
    name = line.strip()
    if judge(name):
        if lenth < len(name):
            lenth = len(name)
            flag = name
           
print flag

f.close()
