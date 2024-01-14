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