n = int(input())
A = 'A'
B = 'B'
C = 'C'
def hannoi(n, A, B, C):
    if not n:
        return
    else:
        hannoi(n-1, A, C, B)
        print "Move", n, "from", A, "to", C
        hannoi(n-1, B, A, C)
hannoi(n, A, B, C)
