# 8 - Argument hints

class Person():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

def veryComplexFunc(a, b, c, d, e, f):
    '''Some function with lots of input
    a: the number of ...
    b: a string of ...
    '''
    return f"{a}, {b}, {c}, {d}, {e}, {f}"


veryComplexFunc(1, 2, Person('David Jones'), 4, 5, 6)


# def veryComplexFunc(a: int, b: str, c: Person, d, e, f):
#     '''Some function with lots of input
#     a: the number of ...
#     b: a string of ...
#     '''
#     return f"{a}, {b}, {c}, {d}, {e}, {f}"


# veryComplexFunc(1, 2, Person('David Jones'), 4, 5, 6)
