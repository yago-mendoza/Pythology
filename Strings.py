##----------------------------------------------------------------------------------------------
## 1.2 Strings
##----------------------------------------------------------------------------------------------

t = 'any_word'

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