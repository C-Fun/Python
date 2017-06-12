def Palindrome_number(num):
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

for i in range(10, 100):
    if(Palindrome_number(i)):
        for j in range(100, 1000):
            if(Palindrome_number(j)):
                for k in range(1000, 10000):
                    if(Palindrome_number(k) and i+j == k):
                        print i, j, k
        
