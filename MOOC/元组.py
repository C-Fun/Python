# -*- coding: cp936 -*-
###交换两个值###
###temp = a###
###a = b   ###
###b = temp###

###元组(不可修改)###
a = 1
b = 2
a, b = b, a

print a, b

###切分一个邮件地址###
name, domain = 'car@hit.edu.cn'.split('@')

print name
print domain

###同时返回列表中最大最小值###
def max_min(lst):
    max = min = lst[0]
    for i in lst:
        if i > max:
            max = i
        if i < min:
            min = i
    return max, min

###DSU模式###
###根据单词的长度对一个单词列表进行排序###
def sort_by_length(words):
    # decorate(装饰)
    t = []
    for word in words:
        t.append(len(word), word)

    #sort(排序)
    t.sort(reverse = True)

    #undecorate(反装饰)
    res = []
    for length, word in t:
        res.append(word)

    return res
######################################
words = ['abcde', 'defgh', 'df', 'lsfgq']
lst = []
for word in words:
    lst.append((len(word), word))

lst.sort(reverse = True)

res = []
''' 'length, word'是lst中的一个元组 '''
for length, word in lst:
    res.append(word)
    
print res
