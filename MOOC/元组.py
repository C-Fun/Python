# -*- coding: cp936 -*-
###��������ֵ###
###temp = a###
###a = b   ###
###b = temp###

###Ԫ��(�����޸�)###
a = 1
b = 2
a, b = b, a

print a, b

###�з�һ���ʼ���ַ###
name, domain = 'car@hit.edu.cn'.split('@')

print name
print domain

###ͬʱ�����б��������Сֵ###
def max_min(lst):
    max = min = lst[0]
    for i in lst:
        if i > max:
            max = i
        if i < min:
            min = i
    return max, min

###DSUģʽ###
###���ݵ��ʵĳ��ȶ�һ�������б��������###
def sort_by_length(words):
    # decorate(װ��)
    t = []
    for word in words:
        t.append(len(word), word)

    #sort(����)
    t.sort(reverse = True)

    #undecorate(��װ��)
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
''' 'length, word'��lst�е�һ��Ԫ�� '''
for length, word in lst:
    res.append(word)
    
print res
