n = int(input())
Sum = 0

def fib(n):
    f1, f2 = 0, 1
    global Sum
    while(True):
        f1, f2 = f2, f1 + f2
        if(f2 > n):
            break
        elif not f2%2:
            Sum += f2

fib(n)
print Sum
