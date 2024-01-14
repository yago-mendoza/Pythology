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