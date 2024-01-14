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