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