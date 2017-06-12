score = int(input("Score: "))
judge = input("If the lesfer get ball(Y/N): ")
last = int(input("The scends last: "))
score -= 3
flag = 1

if judge == 'Y' or judge == 'y':
    score += 0.5
elif  judge == 'N' or judge == 'n':
    score -= 0.5
else:
    flag = 0

if flag:
    if score < 0:
        score = 0
    else:
        score **= 2

    if score > last:
        print ("Safe!")
    else:
        print("Not Safe!")
else:
    print("Input Error!")
    
