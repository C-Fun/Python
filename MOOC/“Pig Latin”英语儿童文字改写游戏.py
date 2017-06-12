def rule1(letter, pos=0):
    if (letter in('a', 'e', 'i', 'o', 'u')) or (letter == 'y' and pos != 0):
        return True
    else:
        return False
    
def rule2(Str):
    return Str + 'hay'

def rule3(Str):
    return Str[2:] + 'quay'

def rule4(Str, num):
    return Str[num:] + Str[:num] + 'ay'

def rule5(Str):
    Str = Str.lower()
    return Str

sentence = raw_input()
newsenten = ''
char = ''
sentence = rule5(sentence)

for i in range(0,len(sentence)):
    if sentence[i]!=' ':
        char += sentence[i]
    else:
        if rule1(char[0]):
            newsenten += rule2(char)
        elif char[:2] == 'qu':
            newsenten += rule3(char)
        else:
            count = 0
            for k in range(0,len(char)):
                if rule1(char[k], k):
                    break
                else:
                    count += 1
            newsenten += rule4(char, count)
        newsenten += ' '
        char = ''
if rule1(char[0]):
    newsenten += rule2(char)
elif char[:2] == 'qu':
    newsenten += rule3(char)
else:
    count = 0
    for k in range(0,len(char)):
        if rule1(char[k], k):
            break
        else:
            count += 1
    newsenten += rule4(char, count)

print newsenten
                
