def Create(dic):
    lst = []
    words = ' '
    for line in range(100):
        words = raw_input()
        lst = words.split()
        for i in range(len(lst)):
            if(not lst[i] in dic):
                dic[lst[i]] = [line]
            else:
                dic[lst[i]].append(line)
        lst = []
        words = ' '

def Print(dic):
    query = {'':[]}
    lst = []
    Sort = []
    lst = sorted(dic.items())
    for i in range(len(lst)):
        Sort[i] = lst[i][0]+': '
        for j in range(1,len(lst[i])):
            query[lst[i][0]].append(lst[i][j])
        for k in range(1,len(lst[i]-1)):
            Sort[i] += lst[i][k] + ', '
        Sort[i] += lst[i][k+1]
        print Sort[i]

def Find(dic):
    Query = []
    lst = []
    words = ' '
    while(words != ''):
        words = raw_input()
        lst = words.split()
        for i in range(len(lst)):
            
