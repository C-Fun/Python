# -*- coding: cp936 -*-
def Judge(num):
    lst = []
    lstPalindrome = []
    remainder = num
    while num:
        remainder = num%10
        num /= 10
        lst.append(remainder)
        lstPalindrome.append(remainder)
    lstPalindrome.reverse()
    if(lst == lstPalindrome):
        return True
    else:
        return False

def main():
    max = 0
    n = int(raw_input())
    for i in range(1, 10**n):
        for j in range(1, 10**n):
            if Judge(j*i) and j*i>max:
                max = j*i
    print max     
main()
