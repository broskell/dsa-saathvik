# Problem Editorial: LC 347 — Top K Frequent Elements

## 1. Problem Statement & Constraints

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.

### Constraints
- $1 \le \text{nums.length} \le 10^5$
- $-10^4 \le \text{nums}[i] \le 10^4$
- $k$ is in the range $[1, \text{number of unique elements in the array}]$.
- It is **guaranteed** that the answer is unique (i.e., the set of top $k$ frequent elements is unique).

---

## 2. Brute Force Approach

### Intuition
Count the frequencies of all elements using a hash map. Convert the dictionary into a list of tuples `(frequency, element)` and sort the entire list in descending order by frequency. Extract the first `k` elements.

### Code
```python
from collections import Counter

def topKFrequent_brute(nums, k):
    counts = Counter(nums)
    sorted_elements = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
    return sorted_elements[:k]
```

### Complexity
- **Time Complexity:** $O(U \log U)$ where $U \le n$ is the number of unique elements. Sorting all unique items costs $O(U \log U)$, which degenerates to $O(n \log n)$ when all elements are distinct.
- **Space Complexity:** $O(U)$ to store the frequency map and list of unique elements.

---

## 3. Key Observation / Core Insight

The superficial observation is simply *"count frequencies using a hash map / Counter"*. However, **the key algorithmic insight** is:

> **You never need to sort all distinct values when you only need the top $k$ items, because element frequencies are bounded between $1$ and $n$.**

Since an element's frequency can never exceed the total array length $n$, we can use **Bucket Sort**: create an array of lists `buckets` of length $n + 1$, where `buckets[freq]` holds all numbers that appear exactly `freq` times. Scanning this bucket structure from index $n$ down to $1$ yields the most frequent elements in strictly **$O(n)$ linear time**, bypassing the $O(n \log n)$ comparison sorting bottleneck entirely.

*(Alternative insight: A Min-Heap of size $k$ maintains the $k$ most frequent elements in $O(n \log k)$ time).*

---

## 4. Optimal Approach (Bucket Sort Solution)

### Algorithm
1. Build a frequency count map using `collections.Counter(nums)`.
2. Initialize an array of empty lists `buckets` of size `len(nums) + 1`.
3. For each `(element, frequency)` pair in the count map, append `element` to `buckets[frequency]`.
4. Iterate backwards through `buckets` starting from index `n` down to `1`:
   - Append elements in `buckets[i]` to `result`.
   - As soon as `len(result) == k`, stop and return `result`.

### Implementation
```python
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
            
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
```

### Complexity
- **Time Complexity:** $O(n)$ — Building the frequency map takes $O(n)$, populating buckets takes $O(U) \le O(n)$, and iterating backward through buckets visits each unique element at most once ($O(n)$ total).
- **Space Complexity:** $O(n)$ — Storing frequency map counts and the bucket array requires $O(n)$ auxiliary space.

---

## 5. Edge Cases & Boundary Conditions

1. **$k$ equals total unique elements / $n = 1$:** E.g., `nums = [1], k = 1`. `buckets[1]` contains `[1]`, immediately returns `[1]`.
2. **All elements identical:** E.g., `nums = [2, 2, 2, 2], k = 1`. `buckets[4]` contains `[2]`, returned instantly.
3. **All elements unique ($k < n$):** E.g., `nums = [1, 2, 3, 4], k = 2`. `buckets[1]` contains `[1, 2, 3, 4]`, picks first $k$ items.
4. **Negative numbers:** Handled seamlessly since hash map keys support all signed integers.

---

## 6. Common Pitfalls & Mistakes

- **Confusing frequency with array indices:** Placing elements in `buckets[num]` instead of `buckets[freq]`. The bucket index MUST represent the *frequency count* of the number.
- **Off-by-one errors in bucket allocation:** Initializing `buckets` with size `len(nums)` instead of `len(nums) + 1`. If an element appears $n$ times, accessing `buckets[n]` would raise an `IndexError`.
- **Assuming Heap is always faster than Bucket Sort:** While Heap $O(n \log k)$ uses less space when $k \ll n$, Bucket Sort strictly guarantees $O(n)$ worst-case time complexity.

---

## 7. Complexity Analysis & Trade-offs

| Approach | Time Complexity | Space Complexity | Notes |
| :--- | :--- | :--- | :--- |
| Full Sorting | $O(n \log n)$ | $O(n)$ | Simple to write, but violates $O(n)$ target. |
| Min-Heap (size $k$) | $O(n \log k)$ | $O(n + k)$ | Excellent when $k \ll n$. |
| **Bucket Sort** | **$O(n)$** | **$O(n)$** | **Optimal $O(n)$ time complexity**, leveraging frequency bounds $1..n$. |
