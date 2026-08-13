# =============================================================
# DSA FUNDAMENTALS -- Pattern Recognition & Problem-Solving Strategy
# =============================================================
# This is a CHEAT SHEET for recognizing which data structures and
# algorithms to use when you encounter common problem patterns.
# As you solve more problems, these patterns will become second nature.

# =============================================================
# PATTERN 1: "Does this value exist?"
# =============================================================
# When a problem asks: "Is X in the list?", "Have we seen this before?",
# "Check if a number is already used", "Find duplicates", etc.
#
# SOLUTION: Use a SET
# Why: Sets have O(1) lookup time -- checking membership is instant

# Example: Check if a number exists in a list
numbers = [1, 2, 3, 4, 5]
num_set = set(numbers)
print(7 in num_set)           # False (fast lookup)

# Example: Find unique values (remove duplicates)
scores = [95, 87, 95, 92, 87, 88]
unique_scores = set(scores)   # {95, 87, 92, 88}

# Example: Track visited nodes in a graph (pseudo-code)
# visited = set()
# visited.add(node1)
# if node2 not in visited:
#     visited.add(node2)

# =============================================================
# PATTERN 2: "How many times does each value occur?"
# =============================================================
# When a problem asks: "Count occurrences", "Frequency of each item",
# "Most common element", "Group by category", etc.
#
# SOLUTION: Use a DICTIONARY (Hash Map)
# Why: Dictionaries map keys to values in O(1) time

# Example: Count word frequencies
text = "hello world hello python hello"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)   # {'hello': 3, 'world': 1, 'python': 1}

# Example: Group students by grade
students = [("Alice", "A"), ("Bob", "B"), ("Charlie", "A")]
grades = {}
for name, grade in students:
    if grade not in grades:
        grades[grade] = []
    grades[grade].append(name)
print(grades)       # {'A': ['Alice', 'Charlie'], 'B': ['Bob']}

# Example: Find most common element
from collections import Counter
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
most_common = Counter(numbers).most_common(1)
print(most_common)  # [(4, 4)]  -- 4 appears 4 times

# =============================================================
# PATTERN 3: "Find something in a SORTED array"
# =============================================================
# When a problem asks: "Search in sorted array", "Find smallest element
# greater than X", "Guess a number game", "Split search space", etc.
#
# SOLUTION: Use BINARY SEARCH
# Why: Eliminates half the search space each time -- O(log n) not O(n)

def binary_search(arr, target):
    """Find target in a sorted array using binary search."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid           # found it
        elif arr[mid] < target:
            left = mid + 1       # search right half
        else:
            right = mid - 1      # search left half
    return -1                    # not found

sorted_nums = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(sorted_nums, 7))   # 3 (index)
print(binary_search(sorted_nums, 8))   # -1 (not found)

# =============================================================
# PATTERN 4: "Process elements in order (first in, first out)"
# =============================================================
# When a problem asks: "Queue", "Breadth-first search", "Process in
# arrival order", "Handle requests", etc.
#
# SOLUTION: Use a QUEUE (collections.deque)
# Why: FIFO ensures elements are processed in the order they arrive

from collections import deque

queue = deque()
queue.append("first")
queue.append("second")
queue.append("third")

while queue:
    process = queue.popleft()  # remove from front
    print(f"Processing: {process}")
# Outputs: first, second, third

# =============================================================
# PATTERN 5: "Process elements in reverse order (last in, first out)"
# =============================================================
# When a problem asks: "Stack", "Depth-first search", "Undo/redo",
# "Evaluate expressions", "Backtracking", etc.
#
# SOLUTION: Use a STACK (list or collections.deque)
# Why: LIFO ensures elements are processed in reverse

stack = []
stack.append("first")
stack.append("second")
stack.append("third")

while stack:
    process = stack.pop()      # remove from top
    print(f"Processing: {process}")
# Outputs: third, second, first

# =============================================================
# PATTERN 6: "Find shortest path / connections"
# =============================================================
# When a problem asks: "Shortest path", "Distance between nodes",
# "Degrees of separation", "Level-order traversal", etc.
#
# SOLUTION: Use BREADTH-FIRST SEARCH (BFS)
# Why: BFS explores level by level, finding shortest path first

# Example: Graph represented as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

def bfs(graph, start, target):
    """Find shortest path from start to target."""
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        node, path = queue.popleft()
        if node == target:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

print(bfs(graph, 'A', 'D'))  # ['A', 'B', 'D']

# =============================================================
# PATTERN 7: "Explore all possibilities / combinations"
# =============================================================
# When a problem asks: "All permutations", "All combinations",
# "Backtrack", "Try all paths", "Generate all subsets", etc.
#
# SOLUTION: Use RECURSION / BACKTRACKING
# Why: Naturally explores all branches and backtracks when needed

def backtrack_subsets(arr, index=0, current=[]):
    """Generate all subsets of an array."""
    result = []

    def helper(index, current):
        result.append(current[:])  # add current subset

        for i in range(index, len(arr)):
            current.append(arr[i])     # choose
            helper(i + 1, current)      # explore
            current.pop()               # unchoose (backtrack)

    helper(0, [])
    return result

print(backtrack_subsets([1, 2, 3]))
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

# =============================================================
# PATTERN 8: "Find maximum/minimum with constraints"
# =============================================================
# When a problem asks: "Max profit", "Max product", "Min cost",
# "Optimize subject to constraints", etc.
#
# SOLUTION: Use DYNAMIC PROGRAMMING or GREEDY
# Why: Builds solution incrementally or makes locally optimal choices

# Example: Knapsack problem (DP)
def knapsack(weights, values, capacity):
    """Find max value with weight limit."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                # include item or exclude it
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

weights = [2, 3, 4]
values = [3, 4, 5]
capacity = 5
print(knapsack(weights, values, capacity))  # 10 (take items 0 and 1)

# =============================================================
# PATTERN 9: "Sort or organize data"
# =============================================================
# When a problem asks: "Sort by", "Arrange in order", "Priority",
# "Custom ordering", etc.
#
# SOLUTION: Use SORT with custom key or comparator
# Why: Organized data makes many other operations easier

# Example: Sort students by GPA (descending)
students = [
    {"name": "Alice", "gpa": 3.8},
    {"name": "Bob", "gpa": 3.5},
    {"name": "Charlie", "gpa": 3.9}
]
sorted_students = sorted(students, key=lambda s: s["gpa"], reverse=True)
print([s["name"] for s in sorted_students])  # ['Charlie', 'Alice', 'Bob']

# =============================================================
# PATTERN 10: "Paired elements / two-pointer technique"
# =============================================================
# When a problem asks: "Two sum", "Container with most water",
# "Pairs that sum to target", "Merge sorted arrays", etc.
#
# SOLUTION: Use TWO POINTERS
# Why: Efficiently finds pairs without nested loops

def two_sum(arr, target):
    """Find two numbers that sum to target in sorted array."""
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [arr[left], arr[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

sorted_arr = [2, 3, 5, 7, 11]
print(two_sum(sorted_arr, 8))  # [3, 5]

# =============================================================
# YOUR PROBLEM-SOLVING WORKFLOW
# =============================================================
# 1. READ the problem carefully -- what is it really asking?
# 2. IDENTIFY the pattern -- does it match one from above?
# 3. CHOOSE the right data structure / algorithm
# 4. IMPLEMENT with clear logic and handle edge cases
# 5. TEST with examples (especially edge cases)
# 6. OPTIMIZE if needed (time/space complexity)
#
# As you solve more problems, pattern recognition becomes automatic.
# Start collecting problems and tag them by pattern.
# Your brain will learn the connections over time.
# =============================================================
