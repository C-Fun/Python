import math
a = 10
b = 40
c = 15
x1 = -(b/(2*a)) + math.sqrt(b**2 - 4*a*c)/(2*a)
x2 = -(b/(2*a)) - math.sqrt(b**2 - 4*a*c)/(2*a)
print('{:.2f}'.format(x2),'{:.2f}'.format(x1))

money = 1000
i = 0
for i in range(0,10):
    money *= 1.047
    money += 1000

print ('{:.2f}'.format(money-1000))
