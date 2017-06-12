n = int(raw_input())
LST = []
lst = []
end = []


for i in range(n):
    lst.append('1')
    if(i>1):
        for j in range(i-1):
            lst.append(str(eval(LST[i-1][j])+eval(LST[i-1][j+1])))
    if(i>0):
        lst.append('1')
    LST.append(lst)
    lst = []

for i in range(n):
    for j in range(n-i-1):
        lst.append(' ')
    end.append("".join(lst) + " ".join(LST[i]))
    lst = []

for i in range(n):
    print end[i]
    
