import re
import keyword

def judge(string):
    if keyword.iskeyword (string):
        return False
    elif re.match('[a-zA-Z]', string) != None or \
         re.match('_', string) != None:
        return True
    else:
        return False

for i in range(6):
    string = raw_input()
    print judge(string)
