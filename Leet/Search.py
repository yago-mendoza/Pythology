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