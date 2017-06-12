def foo():
    m = 1
    def bar():
         n = 2
         return m + n
    m = bar()
    print m
foo()
