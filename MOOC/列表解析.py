# -*- coding: utf-8 -*-
lst = []

##############################
###生成值为{x²:x∈{1...9}}的列表#
##############################
###for x in range(1, 10):    #
###    lst.append(x**2)      #
##############################

####列表解析法###################
####生成值为{x²:x∈{1...9}}的列表#
lst = [x**2 for x in range(1, 10)]

print lst
