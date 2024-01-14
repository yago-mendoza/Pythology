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