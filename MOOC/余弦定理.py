import math
a = float(input())
b = float(input())
c = float(input())
C = math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b)))
print'{:.1f}'.format(C)
