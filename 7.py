# 7: generator for storing internal states

def getFib(n):
    '''Return the n-th item in a Fibonacci series'''
    a, b = 1, 1
    for i in range(n-2):
        a, b = b, a+b
    return b

getFib(2)

def getFibG():
    a, b = 1, 1
    while True:
        yield b
        a, b = b, a+b
    
g = getFibG()
next(g)

# yield can also be used to accept information
# x = yield
