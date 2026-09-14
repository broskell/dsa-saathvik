# Problem Editorial: LC 1 — Two Sum

## 1. Problem Statement & Constraints

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the *same* element twice. You can return the answer in any order.

### Constraints
- $2 \le \text{nums.length} \le 10^4$
- $-10^9 \le \text{nums}[i] \le 10^9$
- $-10^9 \le \text{target} \le 10^9$
- Exactly one valid answer exists.

---

## 2. Brute Force Approach

### Intuition
Check every possible pair of indices $(i, j)$ where $i \neq j$. For each pair, calculate their sum and check if it equals `target`.

### Code
```python
def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```

### Complexity
- **Time Complexity:** $O(n^2)$ — Nested loops check $\frac{n(n-1)}{2}$ pairs. For $n = 10^4$, this results in $\approx 5 \times 10^7$ operations.
- **Space Complexity:** $O(1)$ — Uses no extra memory beyond basic loop counters.

---

## 3. Key Observation / Core Insight

Instead of scanning forward through the array repeatedly to find the partner value `target - current_val`, **remember what has already been passed**.

When standing at index `i` with value `v`, the missing partner required to reach `target` is `complement = target - v`. If we store previously visited elements in a data structure that provides $O(1)$ lookup (a hash map), we can ask in constant time: *"Have I already seen my required partner?"*

---

## 4. Optimal Approach

### Algorithm
1. Initialize an empty hash map `seen` to store `element_value -> index`.
2. Iterate through `nums` using index `i` and value `v`.
3. Calculate `complement = target - v`.
4. Check if `complement` exists as a key in `seen`:
   - If **yes**: Return `[seen[complement], i]`.
   - If **no**: Insert `seen[v] = i` into the hash map.
5. Continue iteration. (The problem guarantees a solution will be found).

### Implementation
```python
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            complement = target - v
            if complement in seen:
                return [seen[complement], i]
            seen[v] = i
        return []
```

### Complexity
- **Time Complexity:** $O(n)$ — Single pass through the array. Hash map insertions and lookups take $O(1)$ amortized time.
- **Space Complexity:** $O(n)$ — In the worst case, we store up to $n - 1$ elements in the hash map before finding the matching pair.

---

## 5. Edge Cases & Boundary Conditions

1. **Negative numbers & Zeroes:** Works seamlessly because arithmetic complements `target - v` and hash map keys support negative integers and zero.
2. **Duplicate values in `nums`:** E.g., `nums = [3, 3], target = 6`. When checking `v = 3` at `i = 1`, the map already contains the earlier `3` from index `0`. The complement check happens *before* overwriting/adding `seen[v]`, preventing self-matching.
3. **Smallest array size ($n = 2$):** Correctly checks index 1 against index 0 on the second iteration step.

---

## 6. Common Pitfalls & Mistakes

- **Two-Pass Hash Map with Key Collisions:** Creating a hash map of all elements upfront first (`seen[v] = i`) overwrites duplicate values (e.g. `[3, 3]`), causing index loss or returning the same index twice ($i = j$).
- **Using List Search Inside Loop:** Writing `if (target - v) in nums` inside a loop creates a hidden $O(n^2)$ time complexity because list membership checking is $O(n)$.
- **Returning values instead of indices:** The problem explicitly requests *indices* `[i, j]`, not the numbers `[nums[i], nums[j]]`.

---

## 7. Complexity Analysis & Trade-offs

| Approach | Time Complexity | Space Complexity | Notes |
| :--- | :--- | :--- | :--- |
| Brute Force | $O(n^2)$ | $O(1)$ | No extra memory, but TLE for large $n$. |
| Sorting + Two Pointers | $O(n \log n)$ | $O(n)$ | Requires sorting and preserving original indices. |
| **One-Pass Hash Map** | **$O(n)$** | **$O(n)$** | **Optimal time complexity** by trading space for speed. |
