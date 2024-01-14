### Table of Contents

# 1. Basic Python ..................................................... Line 117

#   1.1 General ....................................................... Line
#       1.1.1  Binary ................................................. Line
#       1.1.2 Falsey Values ........................................... Line
#       1.1.3 Type checking ........................................... Line 
#   1.2 Strings ....................................................... Line
#       1.2.1 Basic Methods ........................................... Line
#       1.2.2 Search Methods .......................................... Line
#       1.2.3 Formatting .............................................. Line
#       1.2.4 Replacing ............................................... Line
#   1.3 Lists ......................................................... Line 229
#       1.3.1 Merging lists ........................................... Line
#       1.3.2 Removing elements ....................................... Line
#       1.3.3 Slicing ................................................. Line
#   1.4 Dictionaries .................................................. Line 260
#       1.4.1 Merging dictionaries .................................... Line
#       1.4.2 Accessing values ........................................ Line
#       1.4.3 The 'setdefault' method ................................. Line
#   1.5 Functions ..................................................... Line 292
#       1.5.1 One-liner functions ..................................... Line
#       1.5.2 Unpacking arguments within the function call ............ Line
#       1.5.3 Args & Kwargs ........................................... Line
#   1.6 Keywords ...................................................... Line 328
#       1.6.1 The 'max' and 'min' functions ........................... Line
#       1.6.2 The 'enumerate' function ................................ Line
#       1.6.3 The 'zip' function ...................................... Line

# 2. Advanced Python .................................................. Line

#   2.1 Flow Structures ............................................... Line
#       2.1.1 The 'break-else' pair ................................... Line
#       2.1.2 The 'continue' keyword .................................. Line
#   2.2 Iterators ..................................................... Line 376
#       2.2.1 Class and function (generator) implementations .......... Line
#       2.2.2 The 'map' keyword ....................................... Line
#       2.2.3 The 'filter' keyword .................................... Line
#   2.3 Comprehension Expressions ..................................... Line 416
#       2.3.1 List Comprehension ...................................... Line
#       2.3.2 Dictionary Comprehension ................................ Line
#       2.3.3 Iterator Comprehension .................................. Line

# 3. Special Features ................................................. Line 454

#   3.1 The Walrus Operator ........................................... Line
#       3.1.1 Debugging complex expressions ........................... Line
#       3.1.2 Avoiding double definitions ............................. Line
#       3.1.3 Avoid double calls in comprehension expressions ......... Line
#       3.1.4 Capturing values on "any/all" functions ................. Line
#       3.1.5 Input invoices .......................................... Line
#   3.2 The 'match' keyword ........................................... Line 499

# 4. Algoritmic Thinking .............................................. Line

#   4.1 Combinations and Permutations ................................. Line
#       4.1.1 Simple Combination Through List Comprehension ........... Line
#   4.2 Search and Selection .......................................... Line 554
#       4.2.1 Finding Indices of Numbers That Add Up to Target ........ Line
#       4.2.2 Check for Duplicate in List ............................. Line
#       4.2.3 Find Closest Integer to Zero ............................ Line
#       4.2.4 Find First Missing Number in Sequence ................... Line
#       4.2.5 Missing Integer Finder .................................. Line
#       4.2.6 Find Word with the Most Vowels .......................... Line
#       4.2.7 First Non-repeated List Element ......................... Line
#       4.2.8 Max Subset Sum No Adjacent .............................. Line
#   4.3 Mathematics and Statistics .................................... Line 667
#       4.3.1 Odd Number Checker ...................................... Line
#       4.3.2 Minimal Absolute Sum Difference ......................... Line
#       4.3.3 Prime Checker ........................................... Line
#       4.3.4 Max Like-Time Coefficient ............................... Line
#   4.4 String Manipulation ........................................... Line
#       4.4.1 Character Frequency Dictionary .......................... Line
#       4.4.2 Longest Valid Password .................................. Line
#   4.5 Data Structures Manipulation .................................. Line
#       4.5.1 Sort Dictionary by Age .................................. Line
#       4.5.2 String Frequency in List ................................ Line
#       4.5.3 Array Rotation .......................................... Line
#   4.6 Recursivity ................................................... Line 802
#       4.6.1 Longest Palindromic Subsequence ......................... Line
#       4.6.2 Climbing Stairs Unique Ways ............................. Line
#       4.6.3 Max Subset Sum No Adjacent .............................. Line
#   4.7 Greedy Algorithms ............................................. Line 845
#       4.7.1 Point Color Balance Detection ........................... Line
#       4.7.2 Maximum Profit in Job Scheduling ........................ Line
#       4.7.3 Minimum Number of Arrows to Burst Balloons .............. Line
# 5. Annexes .......................................................... Line

# SHORTCUT : CTRL + G + < n_line > + ENTER 

################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################

'''
████████████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████ ▄▄▄ █ ▄▄ █▄ ▄▄▀██ ▄ ██▄ ▄███▄ ▄█ ▄ ▄ █▄ █ ▄██████████████████████████
██████████████████████████ ███▀█ ██ ██ ██ ██ ▀ ███ ██▀██ ████ ████▄ ▄███████████████████████████
██████████████████████████▄▄▄▄▄█▄▄▄▄█▄▄▄▄██▄▄█▄▄█▄▄▄▄▄█▄▄▄██▄▄▄███▄▄▄███████████████████████████
'''

import math
import time

## General Advice

# - Sorting is always a good idea.
# - You might have done some assumptions that are overcomplicating things.
# - Make sure to consider all edge cases, like empty list etc.
# - Sometimes long code snippets are the only solution.

################################################################################################
## 1. General Python
################################################################################################

##----------------------------------------------------------------------------------------------
## 1.1 General
##----------------------------------------------------------------------------------------------

# WRONG : if var != 0 and var != 1  (RIGHT : if var not in {0,1})
# WRONG : if lst != []              (RIGHT : if lst)
# WRONG : if e == " "               (RIGHT : if e.isspace())
# WRONG : if x > 0 and x < 1        (RIGHT : if 0 < x < 1)

## 1.1.1 Binary

bn = bin(5)[2:] # >> 101

## 1.1.2 Falsey values

# Falsey values are the following
falsey_values = [0, None, False, [], {}, ""]

not all(falsey_values) # >>> True (there's some falsy value)
not any(falsey_values) # >>> True (all of them are falsy values)

# We can avoid falsy values by fallback declaration
t = 0 or 1 # instead of 'return r if r else 1'

## 1.1.3 Type checking

# The 'type' keyword works just fine.
type(t) is str
# Yet, 'isinstance' is THE good practice.
# It supports both types and classes (including inheritance and multi-check).
class Fruit : pass
class Apple(Fruit) : pass
isinstance(Apple(), Fruit) # >>> True
isinstance(Apple(), Apple) # >>> True
isinstance(Apple(), (str, Apple, int)) # >> True (at least one)
# Type does not support inheritance.
type(Apple()) is Apple # >>> True
type(Apple()) is Fruit # >>> ¡False!

##----------------------------------------------------------------------------------------------
## 1.2 Strings
##----------------------------------------------------------------------------------------------

## 1.2.1 Basic Methods

t = t.strip(), t.strip('a')
t = t.lstrip(), t.lstrip('b')
t = t.rstrip(), t.rstrip('c')

t.startswith('a'), t.endswith(' b')

t.isalpha(), t.isalnum(), t.isdigit()
t.islower(), t.isupper()
t.upper(), t.lower()
t.capitalize()

t.count('a')

"-".join(['hello', 'world'])

"a=b=c".split("=")  # ['a', 'b', 'c']
"a=b=c".partition("=")  # ('a', '=', 'b', '=', 'c')

## 1.2.2 Search Methods

# Both individual characters and substrings
t.find('a') # if not find, returns -1
t.rfind('a') # last occurrence

## 1.2.3 Formatting

# f-strings
n, A = 18.551, 31.33
print(f'Output : num = {n}; area = {A}')
print('Output : num = {}; area = {}'.format(n, A))

# Be mindful that f-strings can contain conditional expressions
f'{"One" if bn == 1 else "Zero"}'

f'{t:^25}' or t.center(25) # center padding
f'{t:<25}' or t.ljust(25) # left padding
f'{t:>25}' or t.rjust(25) # right padding

# By default, spaces will be inserted.
# You can use any other single character for padding.
f'{t:*^25}' or t.center(25,'*')

# Padding numbers with zeros
f'{t:05}' or f'{t:0>5}'

f'{t:.5}' # keeps up to 5 characters (truncating)
f'time = {n:.2f}' # rounds to 2 decimal places (round)
f'{n:10.2f}' # would pad then round

## 1.2.4 Replacing

s = "Hello, World"
s.replace('e','E') # replaces every occurrence

# Multiple (translate tables)
legend = str.maketrans({'a':'A','b':'B','c':'C'})
legend = str.maketrans('abc','ABC')
s.translate(legend)

# Removing multiple characters
legend = str.maketrans("", "", "aeiou")
s.translate(legend) # deletes all vocals

##----------------------------------------------------------------------------------------------
## 1.3 Lists
##----------------------------------------------------------------------------------------------

range(5)
range(2, 5)
range(0, 10, 2)
range(5, 0, -1)

## 1.3.1 Merging lists

lst1, lst2 = [1,2,3,4], [5,6,7,8]
lst = lst1 + lst2 # or lst1.extend(lst), but affects lst1
lst = [*lst1, *lst2] # '*' used to unpack
# >>> [1,2,3,4,5,6,7,8]

## 1.3.2 Removing elements

lst.remove['a']
v = lst.pop(-1) # we can keep it
lst = lst[:-1] # (6)
lst.remove(lst[lst.index(5)])

## 1.3.3 Slicing

lst[:] # [1,2,3,4]
lst[2:3] # [3] (same as lst3[2])
lst[-4:-1] # [1,2,3]
lst[1::1] # [2,3,4]
lst[::-1] # [4,3,2,1]

##----------------------------------------------------------------------------------------------
## 1.4 Dictionaries
##----------------------------------------------------------------------------------------------

## 1.4.1 Merging dictionaries

d1, d2 = {'a':'z','b':'b'}, {'a':'a', 'c':'c'}
d1.update(d2) # d1 >> {'a':'a', 'b':'b', 'c':'c'}
d3 = {**d1, **d2, **{'d':'d'}} # merges as many as wanted
# Yet the most useful way to do so is.
d1 | d2 | d3

## 1.4.2 Accessing values

d1['a']
d1.get('a')
d1.get('z',0) # fallback value

# Great structure
for key, value in dict.items() :
    continue

## 1.4.3 The 'setdefault' method

# Respects value if already exists, and returns the located value.
students = {'Ben':{'Maths':8.2}}
alice = students.setdefault('Alice',{})
alice['English'] = 9.5
ben = students.setdefault('Ben',{}) # Does nothing because it already exists
ben['English'] = 6.0
# >> {'Ben': {'Maths': 8.2, 'English': 6.0}, 'Alice': {'English': 6.0}}

##----------------------------------------------------------------------------------------------
## 1.5 Functions
##----------------------------------------------------------------------------------------------

## 1.5.1 One-liner functions

def f(a,b,c): print(a,b,c)
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

##----------------------------------------------------------------------------------------------
## 1.6 Keywords
##----------------------------------------------------------------------------------------------

## 1.6.1 The 'max' & 'min' functions

max([]) # >> Error (if lst happens to be empty) [watch out]
max(lst, key=len)

## 1.6.2 The 'enumerate' function

for index, item in enumerate(lst):
    continue

## 1.6.3 The 'zip' function

for name, age, gender in zip(lst, lst1, lst2):
    continue

################################################################################################
## 2. Advanced Python
################################################################################################

##----------------------------------------------------------------------------------------------
## 2.1 Flow structures
##----------------------------------------------------------------------------------------------

## 2.1.1 The 'continue' keyword

values = 0
for num in lst:
    if num < 0 or num % 2: continue
    values += num

## 2.1.2 The 'break-else' pair

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        # Extra: N is prime ⟺ ∄i∈[2,int(sqrt(N))] : N%i=0
        if n % i == 0:
            print(f"{n} is not prime.")
            break
    else:
        # Activates if the 'break' hasn't
        print(f"{n} is prime.")

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

##----------------------------------------------------------------------------------------------
## 2.3 Comprehension Expressions
##----------------------------------------------------------------------------------------------

## 2.3.1 List Comprehension

[x**2 for x in range(5)] # operation
[x for x in range(10) if x % 2 == 0] # filtering
[x for x in range(100) if x % 2 == 0 if x % 5 == 0] # multiple filters
[x if x % 2 == 0 else None for x in range(10)] # fallback shift

[x**2 if 4 < x**2 < 64 else None for x in range(10) if x % 2 == 0] # operation + filter + fallback shift

## Double Loops

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[x for row in M for x in row]

# Now that we have two elements available, we can construct more complex items.
[(i, j, i*j) for i in range(1, 6) for j in range(1, 6)] # cartesian product
[[row[i] for row in M] for i in range(len(M[0]))] # transposing
[[1 if i == j else 0 for j in range(3)] for i in range(3)] # diagonal matrix
# Note. Operations, filters and fallback shifts are still available

## 2.3.2 Dictionary Comprehension

d = {x: x**2 for x in range(10)}
d = {a: b for a,b in zip(lst1, lst2)}
# ...

## 2.3.3 Iterator Comprehension

squares = (num**2 for num in range(10))
evens = (num for num in range(10) if num % 2 == 0)
cartesian_product = ((i, j) for i in range(3) for j in range(3))
wrapped_numbers = (f"The number is {num}" for num in range(5))

################################################################################################
## 3. Special Features
################################################################################################

##----------------------------------------------------------------------------------------------
## 3.1 The Walrus Operator
##----------------------------------------------------------------------------------------------

(walrus := True) # must wear parentheses

# 3.1.1 Debugging complex expressions

2 * n * math.asin(
    math.sqrt(
        (term_1 := (28 - 22) / 2 ** 2)
        + 5 / math.cos(term_2 := 78/11)
    )
)

print(term_1, term_2)

# 3.1.2 Avoiding double definitions

description = {
    "length": (len_numbers := len(A)),
    "sum": (sum_numbers := sum(A)),
    "mean": sum_numbers / len_numbers
}

# 3.1.3 Avoid double calls in comprehension expressions

slowf = lambda x : time.sleep(1<<4)
numbers = [7, 6, 1, 4, 1, 8, 0, 6]
results = [slowf(num) for num in numbers if slowf(num) > 0]
# To avoid repetition
results = [value for num in numbers if (value := slowf(num)) > 0]

# 3.1.4 Capturing values on "any/all" functions

any((witness := v).startswith('H') for v in lst) # witness is assigned with the first 'H' value

# 3.1.5 Input invoices

if (response := input('Y/N : ')) in {'y','Y'} : pass

##----------------------------------------------------------------------------------------------
## 3.2 The 'match' keyword
##----------------------------------------------------------------------------------------------

# The match-case structure is a newer Python feature that is useful
# for handling complex decision trees with many cases.

def calculate(operation, a, b):

    match operation:
        case "add":
            return a + b
        case "subtract":
            return a - b
        case "multiply":
            return a * b
        case "divide":
            # Guard against division by zero
            return "Error: Division by zero" if b == 0 else a / b
        case _:
            # Fallback for unknown operations
            return "Unknown operation"

# However, for simple cases with a limited set of possible operations,
# a dictionary-based approach is typically more concise and just as readable.

def calculate(op, a, b):
    # This is often cooler in regular Python usage due to its simplicity.
    operations = {
        "add": lambda: a + b,
        "subtract": lambda: a - b,
        "multiply": lambda: a * b,
        "divide": lambda: "Error: Division by zero" if b == 0 else a / b
    }
    # Execute the function corresponding to the provided operation, or return
    # a default value if the operation is unknown.
    return operations.get(op, lambda: "Unknown operation")()

################################################################################################
## 4. Algoritmic Thinking
################################################################################################

##----------------------------------------------------------------------------------------------
## 4.1 Combinations and Permutations
##----------------------------------------------------------------------------------------------

# ==============================================
# > Simple combination through list comprehension
# Signature : (lst: List[int]) -> List[Tuple[int, int]])
# Objective : All possible combinations (not permutations)
# Test case : (lst: [1,2,3]) -> [(1, 2), (1, 3), (2, 3)]
# ==============================================
def solution(lst):
    return [(x, y) for index, x in enumerate(lst) for y in lst[index + 1:]]

##----------------------------------------------------------------------------------------------
## 4.2 Search and selection
##----------------------------------------------------------------------------------------------

# ====================================
# > Bitwise XOR as Unique Value Finder
# Signature: (lst: List[int]) -> int
# Objective: Identify the unique element that appears only once in a list where all other elements appear twice.
# Test case: (lst: [1, 2, 3, 1, 2]) -> 3
# ======================================
def solution(lst):
    result = 0
    for num in lst:
        result ^= num
    return result

# ==============================================
# > Finding indices of numbers that add up to target
# Signature : (A: List[int], target: int) -> List[int])
# Objective : The indices of the first two numbers such that they add up to target.
# Test case : (A: [2,4,5,9,5], target: 9) -> [1,2]
# ==============================================
def solution(A, target):
    prevMap = {}
    for i, n in enumerate(A):
        if (diff := target - n) in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

# ==============================================
# > Check for duplicate in list
# Signature: (A: List[int]) -> bool
# Objective: Determine if a list contains any duplicates.
# Test case: (A: [1,2,3,1]) -> True
# ==============================================
def solution(A):
    return len(A) != len(set(A)) # 
    return not any(A.count(x) > 1 for x in set(A)) # O(n^2)

# ==============================================
# > Find closest integer to zero
# Signature: (lst: List[float]) -> float
# Objective: Identify the number closest to zero.
# Test case: (lst: [5.5, -3.2, 7.7, 0.8, -0.5]) -> -0.5
# ==============================================
def solution(lst):
    return min(lst, key=abs)

# ==============================================
# > Find first missing number in sequence
# Signature: (A: List[int]) -> int
# Objective: Find the smallest missing number in a list.
# Test case: (A: [1, 2, 4, 6]) -> 3
# ==============================================
def solution(A):
    A_set = set(A)
    return next((num for num in range(min(A), max(A) + 1) if num not in A_set), None)

# ==============================================
# > Missing Integer Finder
# Signature: (A: List[int]) -> int
# Objective: Find the ONLY missing integer in a sequence.
# Test case: (A: [2, 3, 1, 5]) -> 4
# ==============================================
def solution(A):
    N = len(A) + 1
    total = N * (N + 1) // 2  # Calculated using the sum of a sequence formula
    return total - sum(A)
# Explanation: The sum of numbers from 1 to N is subtracted from the sum of the array.

# ==============================================
# > Find word with the most vowels
# Signature: (lst: List[str]) -> str
# Objective: Find the word with the highest vowel count.
# Test case: (lst: ["apple", "banana", "cherry", "date", "elderberry"]) -> "elderberry"
# ==============================================
def solution(lst):
    return max(lst, key=lambda w: sum(1 for char in w if char in 'aeiouAEIOU'))

# ==============================================
# > First Non-repeated List Element
# Signature: (lst: List[int]) -> int
# Objective: Find the first non-repeated element in a list.
# Test case: (lst: [1, 2, 5, 6, 5, 2, 2, 1]) -> 6
# ==============================================
def solution(lst):
    return next((x for x in lst if lst.count(x) == 1), None)

# ==============================================
# > Max Subset Sum No Adjacent
# Signature: (A: List[int]) -> int
# Objective: Find the global maximum sum of an arbitrary number of elements in the array with a minimum separation of 2.
# Test case: (A: [3, 2, 7, 10]) -> 13
# ==============================================
    # Variables a and b serve as delayed storages, allowing sums to include a
    # number only when it's two steps removed from the last included number.
    # This setup ensures that we maximize the sum according to the problem's
    # separation requirement.
    #________________________________#
    #                         c=500  #
    #                    c=8   b=8   #   
    #              c=7   b=7   a=7   #   
    #        c=7   b=7   a=7         #
    #  c=1   b=1   a=1               #
    #  b=0   a=0                     #
    #  a=0                           #
    #________________________________#
    #   1     7     2     7    500   #
    a = b = c = 0
    for n in A:
        a, b, c = b, c, max(c, a + n)
    return c

##----------------------------------------------------------------------------------------------
## 4.3 Mathematics and Statistics
##----------------------------------------------------------------------------------------------

# ==============================================
# > Odd Number Checker
# Signature: (N: int) -> bool
# Objective: Check if a number is odd using bitwise AND.
# Test case: (N: 3) -> True
# ==============================================
def solution(n):
    return bool(n & 1)

# ==============================================
# > Minimal Absolute Sum Difference
# Signature: (A: List[int]) -> int
# Objective: Find minimal absolute sum difference after splitting array.
# Test case: (A: [3, 1, 2, 4, 3]) -> 1
# ==============================================
def solution(A):
    total_sum = sum(A)
    running_sum = 0
    min_difference = float('inf')
    for i in range(len(A)-1):
        running_sum += A[i]
        difference = abs(2 * running_sum - total_sum)
        min_difference = min(min_difference, difference)
    return min_difference

# ==============================================
# > Prime Checker
# Signature: (N: int) -> None
# Objective: Print whether an integer is prime.
# Test case: (N: 11) -> "11 is prime."
# ==============================================
def solution(N: int) -> None:
    if N <= 1:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            print(f"{N} is not prime.")
            break
    else:
        print(f"{N} is prime.")

# ==============================================
# > Max Like-Time Coefficient
# Signature: (A: List[int]) -> int
# Objective: Return the maximum sum of like-time coefficient after preparing some dishes.
# Each dish's like-time coefficient is the product of its satisfaction level and its position
# in the sequence of prepared dishes. The chef can discard some dishes and reorder the rest
# to maximize this sum.
# Test case: (A: [-1,-8,0,5,-9]) -> 14
# ==============================================
def solution(A):
    A.sort(reverse=True)
    total = maxLikeTime = 0
    for sat in A:
        total += sat
        if total <= 0: break
        maxLikeTime += total
    return maxLikeTime

##----------------------------------------------------------------------------------------------
## 4.4 String Manipulation
##----------------------------------------------------------------------------------------------

# ==============================================
# > Character Frequency Dictionary
# Signature: (text: str) -> Dict[str, int]
# Objective: Convert a string to a frequency dictionary of its characters, sorted by frequency in descending order.
# Test case: (text: 'sort_me_please') -> {'e': 3, '_': 2, 's': 2, 'o': 1, 'm': 1, 'p': 1, 'l': 1, 't': 1, 'r': 1, 'a': 1}
# ==============================================
def solution(text):
    cf = {ch: text.count(ch) for ch in set(text)}
    return dict(sorted(cf.items(), key=lambda item: item[1], reverse=True))

# ==============================================
# > Longest Valid Password
# Signature: (S: str) -> int
# Objective: Find the longest valid password in a string.
#   - The word should contain only alphanumerical characters (a-z, A-Z, 0-9).
#   - The word should have an even number of letters.
#   - The word should have an odd number of digits.
#   If no valid password exists, return -1.
# Test case: (S: "test 5a4bb2") -> 7
# ==============================================
def aux(password: str) -> bool:
    if password.isalnum():
        n_letters = sum(1 for _ in password if _.isalpha())
        n_digits = sum(1 for _ in password if _.isdigit())
        return n_letters % 2 == 0 and n_digits % 2 != 0
    return False

def solution(S: str) -> int:
    candidates = S.split(' ')
    candidates = list(filter(aux, candidates))
    if candidates != []:
        return len(max(candidates,key=len))
    return -1

##----------------------------------------------------------------------------------------------
## 4.5 Data Structures Manipulation
##----------------------------------------------------------------------------------------------

# ==============================================
# > Sort Dictionary by Age
# Signature: (lst: List[Dict[str, int]]) -> List[Dict[str, int]]
# Objective: Sort a list of dictionaries by the 'age' key.
# Test case: (lst: [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}, {"name": "Charlie", "age": 30}]) -> [{"name": "Bob", "age": 20}, {"name": "Alice", "age": 25}, {"name": "Charlie", "age": 30}]
# ==============================================
def solution(lst):
    return lst.sort(key = lambda x : x["age"])
    return sorted(lst, key=lambda x: x["age"])

# ==============================================
# > String Frequency in List
# Signature: (lst: List[str]) -> Dict[str, int]
# Objective: Count the frequency of each string in a list and return a dictionary.
# Test case: (lst: ["apple", "banana", "apple", "orange", "banana", "apple"]) -> {"apple": 3, "banana": 2, "orange": 1}
# ==============================================
def solution(lst):
    return {item: lst.count(item) for item in set(lst)}

# ==============================================
# > Array Rotation
# Signature: (A: List[int], K: int) -> List[int]
# Objective: Rotate an array to the right K times.
# Test case: (A: [1, 2, 3, 4], K: 2) -> [3, 4, 1, 2]
# ==============================================
def solution(A, K):
    if not A: return A # if the array is empty, return it.
    K %= len(A) # Normalize K to be within array length
    return A[-K:] + A[:-K] # Rotate array by slicing and concatenating

##----------------------------------------------------------------------------------------------
## 4.6 Recursivity
##----------------------------------------------------------------------------------------------

# ==============================================
# > Longest Palindromic Subsequence
# Signature: (s: str) -> int
# Objective: Find the length of the longest subsequence in a string which is a palindrome.
# To do so, the string can be edited by substracting characters.
# Test case: (s: "bbbab") -> 4
# ==============================================
def solution(s):
    if not s:
        return 0
    if len(s) == 1:
        return 1
    return 2 + solution(s[1:-1]) if s[0] == s[-1] else max(solution(s[1:]), solution(s[:-1]))

# ====================================
# > Climbing Stairs Unique Ways
# Signature: (n: int) -> int
# Objective: Count the number of distinct ways you can climb to the top of a staircase with n steps, taking 1 or 2 steps at a time.
# Test case: (n: 4) -> 5
# ====================================
def solution(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return n
    # Sum paths from one, two, or three steps back to reach step n.
    memo[n] = solution(n - 1, memo) + solution(n - 2, memo) + solution(n - 3, memo)
    return memo[n]

# ==============================================
# > Max Subset Sum No Adjacent
# Signature: (A: List[int]) -> int
# Objective: Find the global maximum sum of an arbitrary number of elements in the array with a minimum separation of 2.
# Test case: (A: [3, 2, 7, 10]) -> 13
# ==============================================
def solution(A, i=0):
    if i >= len(A): return 0
    return max(A[i] + solution(A, i+2), solution(A, i+1))

##----------------------------------------------------------------------------------------------
## 4.7 Greedy Algorithms
##----------------------------------------------------------------------------------------------

# ==============================================
# > Point Color Balance Detection
# Signature: (X: List[int], Y: List[int], colors: str) -> int
# Objective: Identify the biggest index at which the number of red and green points becomes balanced from a list of points sorted by their distance to the origin.
# Each point is represented as a tuple '(x, y)', with a corresponding color in 'colors' string.
# Test case: (X: [4, 0, 2, -2], Y: [4, 1, 2, -3], colors: 'RGRR') -> 2
# ==============================================
def solution(X, Y, colors):
    pts = [(x**2 + y**2, color) for x, y, color in zip(X, Y, colors)]
    pts.sort(key = lambda x : x[0])
    count = idx = 0
    for i, (_,c) in enumerate(pts):
        count += 1 if c == 'G' else -1
        if count == 0:
            idx = i
    return idx+1 if idx else idx

# ==============================================
# > Maximum Profit in Job Scheduling
# Signature: (jobs: List[Tuple[int, int, int]]) -> int
# Objective: Find the maximum profit by scheduling non-overlapping jobs.
# Each job is represented as a tuple '(start, end, profit)'.
# Test case: (jobs: [(1, 3, 20), (2, 5, 20), (3, 10, 100), (4, 6, 70)]) -> 120
# ==============================================
def solution(jobs):
    jobs.sort(key=lambda x: x[1])  # Sort by end time
    dp = [(0, 0)]  # (end time, max profit)

    for start, end, profit in jobs:
        last_profit = dp[-1][1]
        # Find the last job that does not overlap
        i = next((i for i, (s, p) in enumerate(dp) if s <= start), -1)
        current_profit = dp[i][1] + profit if i != -1 else profit
        if current_profit > last_profit:
            dp.append((end, current_profit))

    return dp[-1][1]

# ==============================================
# > Minimum Number of Arrows to Burst Balloons
# Signature: (points: List[List[int]]) -> int
# Objective: Find the minimum number of arrows that must be shot to burst all balloons.
# Balloons are represented as a list of intervals, where 'points[i]' are the start and end coordinates of the i-th balloon.
# Test case: (points: [[10,16], [2,8], [1,6], [7,12]]) -> 2
# ==============================================
def solution(points):
    if not points:
        return 0

    # Sort by the end coordinate
    points.sort(key=lambda x: x[1])

    arrows = 1
    end = points[0][1]
    for balloon in points:
        if balloon[0] > end:
            arrows += 1
            end = balloon[1]
            
    return arrows

################################################################################################
## 5. Annexes
################################################################################################







































