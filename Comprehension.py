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