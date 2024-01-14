##----------------------------------------------------------------------------------------------
## 4.3 Mathematics and Statistics
##----------------------------------------------------------------------------------------------

# ==============================================
# > Odd Number Checker
# Signature: (N: int) -> bool
# Objective: Check if a number is odd using bitwise AND.
# Test case: (N: 3) -> True
# ==============================================
def solution(n):
    return bool(n & 1)

# ==============================================
# > Minimal Absolute Sum Difference
# Signature: (A: List[int]) -> int
# Objective: Find minimal absolute sum difference after splitting array.
# Test case: (A: [3, 1, 2, 4, 3]) -> 1
# ==============================================
def solution(A):
    total_sum = sum(A)
    running_sum = 0
    min_difference = float('inf')
    for i in range(len(A)-1):
        running_sum += A[i]
        difference = abs(2 * running_sum - total_sum)
        min_difference = min(min_difference, difference)
    return min_difference

# ==============================================
# > Prime Checker
# Signature: (N: int) -> None
# Objective: Print whether an integer is prime.
# Test case: (N: 11) -> "11 is prime."
# ==============================================
def solution(N: int) -> None:
    if N <= 1:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            print(f"{N} is not prime.")
            break
    else:
        print(f"{N} is prime.")

# ==============================================
# > Max Like-Time Coefficient
# Signature: (A: List[int]) -> int
# Objective: Return the maximum sum of like-time coefficient after preparing some dishes.
# Each dish's like-time coefficient is the product of its satisfaction level and its position
# in the sequence of prepared dishes. The chef can discard some dishes and reorder the rest
# to maximize this sum.
# Test case: (A: [-1,-8,0,5,-9]) -> 14
# ==============================================
def solution(A):
    A.sort(reverse=True)
    total = maxLikeTime = 0
    for sat in A:
        total += sat
        if total <= 0: break
        maxLikeTime += total
    return maxLikeTime