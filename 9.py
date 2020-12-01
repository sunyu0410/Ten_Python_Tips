# 9 - debugger

def halve(n): 
    ''' Halve the input'''
    return n / 2


def getFib(n):
    '''Get the n-th number by half in the Fibonacci series.
    Fibonacci series: 1,   1,   2, 3,   5,   8, ...
    Halved:           0.5, 0.5, 1, 1.5, 2.5, 4, ...
    '''
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    result = halve(b)
    return result


print(f'The 3rd item is {getFib(3)}.')
print(f'The 100th item is {getFib(100)}.')

