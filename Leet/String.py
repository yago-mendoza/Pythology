##----------------------------------------------------------------------------------------------
## 4.4 String Manipulation
##----------------------------------------------------------------------------------------------

# ==============================================
# > Character Frequency Dictionary
# Signature: (text: str) -> Dict[str, int]
# Objective: Convert a string to a frequency dictionary of its characters, sorted by frequency in descending order.
# Test case: (text: 'sort_me_please') -> {'e': 3, '_': 2, 's': 2, 'o': 1, 'm': 1, 'p': 1, 'l': 1, 't': 1, 'r': 1, 'a': 1}
# ==============================================
def solution(text):
    cf = {ch: text.count(ch) for ch in set(text)}
    return dict(sorted(cf.items(), key=lambda item: item[1], reverse=True))

# ==============================================
# > Longest Valid Password
# Signature: (S: str) -> int
# Objective: Find the longest valid password in a string.
#   - The word should contain only alphanumerical characters (a-z, A-Z, 0-9).
#   - The word should have an even number of letters.
#   - The word should have an odd number of digits.
#   If no valid password exists, return -1.
# Test case: (S: "test 5a4bb2") -> 7
# ==============================================
def aux(password: str) -> bool:
    if password.isalnum():
        n_letters = sum(1 for _ in password if _.isalpha())
        n_digits = sum(1 for _ in password if _.isdigit())
        return n_letters % 2 == 0 and n_digits % 2 != 0
    return False

def solution(S: str) -> int:
    candidates = S.split(' ')
    candidates = list(filter(aux, candidates))
    if candidates != []:
        return len(max(candidates,key=len))
    return -1