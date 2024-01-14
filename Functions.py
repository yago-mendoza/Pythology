##----------------------------------------------------------------------------------------------
## 1.5 Functions
##----------------------------------------------------------------------------------------------

## 1.5.1 One-liner functions

def f(a,b,c):print(a,b,c)
f = lambda a, b, c : print(a,b,c)
# Indeed, they work with print

## 1.5.2 Unpacking arguments within the function call

def f(a,b,c,d,e,f,g):print(a,b,c,d,e,f,g)
args = ['a','b','c','d','e','f','g']
f(*args)

def f(a,b,c,d): print(a,b,c,d)
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
f(**d)

## 1.5.3 Args & Kwargs

def f (*args):
    for arg in args:
        pass

def f (**kwargs):
    for key, value in kwargs.items():
        pass

# Defaulting arguments

def func_with_defaults(**kwargs):
    defaults = {'var': 12, 'foo': 13}
    return {**defaults, **kwargs}