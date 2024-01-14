##----------------------------------------------------------------------------------------------
## 2.2 Iterators
##----------------------------------------------------------------------------------------------

it = iter(range(3)) # creates iterator from an iterable
next(it) # >>> 0, 1, 2, ..., StopIteration

## 2.2.1 Class and function (generator) implementations

class Counter:
    def __init__ (self, low, high):
        self.curent = low
        self.high = high
    def __iter__ (self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current

def Counter (low, high):
    current = low
    while current <= high:
        yield current
        current += 1

## 2.2.2 The 'map' keyword

nums = list(range(10))
sqrs = map(lambda x : x ** 2, nums) 
# Saves memory by generating the data on te fly.
next(sqrs)
# >>> 0

## 2.2.3 The 'filter' keyword

# Its like a 'map', but the function is conditional.
evens = list(filter(lambda x: x % 2 == 0, range(10)))
# >>> [2, 4, 6, ...]