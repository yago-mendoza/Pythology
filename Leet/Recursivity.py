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