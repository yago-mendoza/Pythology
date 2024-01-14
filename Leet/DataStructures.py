##----------------------------------------------------------------------------------------------
## 4.5 Data Structures Manipulation
##----------------------------------------------------------------------------------------------

# ==============================================
# > Sort Dictionary by Age
# Signature: (lst: List[Dict[str, int]]) -> List[Dict[str, int]]
# Objective: Sort a list of dictionaries by the 'age' key.
# Test case: (lst: [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}, {"name": "Charlie", "age": 30}]) -> [{"name": "Bob", "age": 20}, {"name": "Alice", "age": 25}, {"name": "Charlie", "age": 30}]
# ==============================================
def solution(lst):
    return lst.sort(key = lambda x : x["age"])
    return sorted(lst, key=lambda x: x["age"])

# ==============================================
# > String Frequency in List
# Signature: (lst: List[str]) -> Dict[str, int]
# Objective: Count the frequency of each string in a list and return a dictionary.
# Test case: (lst: ["apple", "banana", "apple", "orange", "banana", "apple"]) -> {"apple": 3, "banana": 2, "orange": 1}
# ==============================================
def solution(lst):
    return {item: lst.count(item) for item in set(lst)}

# ==============================================
# > Array Rotation
# Signature: (A: List[int], K: int) -> List[int]
# Objective: Rotate an array to the right K times.
# Test case: (A: [1, 2, 3, 4], K: 2) -> [3, 4, 1, 2]
# ==============================================
def solution(A, K):
    if not A: return A # if the array is empty, return it.
    K %= len(A) # Normalize K to be within array length
    return A[-K:] + A[:-K] # Rotate array by slicing and concatenating