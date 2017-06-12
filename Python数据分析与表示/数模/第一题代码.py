# -*- coding: utf-8 -*-
"""
Created on Mon May 15 23:32:30 2017

@author: Fun
"""

import xlrd
import matplotlib.pyplot as plt

def Excel_Read(dic):
    file = xlrd.open_workbook('./Book/Book1.xlsx')
    sheet = file.sheets()[0]
    city = sheet.col_values(0)
    for i in range(5):
        people = sheet.col_values(2*i+1)
        GDP = sheet.col_values(2*i+2)
        lst = [[],[],[]]
        for j in range(len(city)):
            if(j>1):
                lst[0].append(city[j])
                lst[1].append(people[j])
                lst[2].append(GDP[j])
        dic[str(2003+i)]=lst

def Sort(dic):
    lst = [[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]]]
    for i in range(len(dic)):
        lst[i] = dic[str(2003+i)]
    
    for i in range(len(lst)):
        length=len(lst[i][2])
        for j in range(length):
            for k in range(length):
                if(k<length-1 and lst[i][2][k]>lst[i][2][k+1]):
                    lst[i][2][k],lst[i][2][k+1]=lst[i][2][k+1],lst[i][2][k]
                    lst[i][1][k],lst[i][1][k+1]=lst[i][1][k+1],lst[i][1][k]
                    lst[i][0][k],lst[i][0][k+1]=lst[i][0][k+1],lst[i][0][k]

    return lst
                    

def Gink(dic):
    gink = {}
    lst = [[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]]]
    lst = Sort(dic)
    for i in range(len(lst)):
        #求收入比重,人口比重
        SumPi = 0
        SumWi = 0
        for j in range(len(lst[i][0])):
            SumPi += lst[i][1][j]
            SumWi += lst[i][2][j]
        G = []
        Pi = 0
        Wi = 0
        Calculate = 0
        for j in range(len(lst[i][0])):
            Pi = lst[i][1][j] / SumPi
            Wi = lst[i][2][j] / SumWi
            Q = 0
            for k in range(j):
                Q += lst[i][2][k] / SumWi
            Calculate += Pi*(2*Q-Wi)
        print 1-Calculate
        
   

'''def Calculate(dic,i,SumPi,SumWi):'''



'''def Paint(gink):



    
def main():
    dic = {}
    gink = {}
    Excel_Read(dic)
    gink = Gink(dic)
    
    
    
main()'''
dic={}
list = [[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]]]
Excel_Read(dic)
'''for i in range(len(dic)):
    lst = dic[str(2003+i)]
    print str(2003+i)
    for j in range(len(lst[0])):
        print lst[0][j],lst[1][j],lst[2][j]

list = Sort(dic)

for i in range(len(list)):
    print str(2003+i)
    for j in range(len(list[i][0])):
        print list[i][0][j],list[i][1][j],list[i][2][j]'''

Gink(dic)
