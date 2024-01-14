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