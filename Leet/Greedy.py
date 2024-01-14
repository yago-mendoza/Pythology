##----------------------------------------------------------------------------------------------
## 4.7 Greedy Algorithms
##----------------------------------------------------------------------------------------------

# ==============================================
# > Point Color Balance Detection
# Signature: (X: List[int], Y: List[int], colors: str) -> int
# Objective: Identify the biggest index at which the number of red and green points becomes balanced from a list of points sorted by their distance to the origin.
# Each point is represented as a tuple '(x, y)', with a corresponding color in 'colors' string.
# Test case: (X: [4, 0, 2, -2], Y: [4, 1, 2, -3], colors: 'RGRR') -> 2
# ==============================================
def solution(X, Y, colors):
    pts = [(x**2 + y**2, color) for x, y, color in zip(X, Y, colors)]
    pts.sort(key = lambda x : x[0])
    count = idx = 0
    for i, (_,c) in enumerate(pts):
        count += 1 if c == 'G' else -1
        if count == 0:
            idx = i
    return idx+1 if idx else idx

# ==============================================
# > Maximum Profit in Job Scheduling
# Signature: (jobs: List[Tuple[int, int, int]]) -> int
# Objective: Find the maximum profit by scheduling non-overlapping jobs.
# Each job is represented as a tuple '(start, end, profit)'.
# Test case: (jobs: [(1, 3, 20), (2, 5, 20), (3, 10, 100), (4, 6, 70)]) -> 120
# ==============================================
def solution(jobs):
    jobs.sort(key=lambda x: x[1])  # Sort by end time
    dp = [(0, 0)]  # (end time, max profit)

    for start, end, profit in jobs:
        last_profit = dp[-1][1]
        # Find the last job that does not overlap
        i = next((i for i, (s, p) in enumerate(dp) if s <= start), -1)
        current_profit = dp[i][1] + profit if i != -1 else profit
        if current_profit > last_profit:
            dp.append((end, current_profit))

    return dp[-1][1]

# ==============================================
# > Minimum Number of Arrows to Burst Balloons
# Signature: (points: List[List[int]]) -> int
# Objective: Find the minimum number of arrows that must be shot to burst all balloons.
# Balloons are represented as a list of intervals, where 'points[i]' are the start and end coordinates of the i-th balloon.
# Test case: (points: [[10,16], [2,8], [1,6], [7,12]]) -> 2
# ==============================================
def solution(points):
    if not points:
        return 0

    # Sort by the end coordinate
    points.sort(key=lambda x: x[1])

    arrows = 1
    end = points[0][1]
    for balloon in points:
        if balloon[0] > end:
            arrows += 1
            end = balloon[1]
            
    return arrows