# Assignment 1.3 Written Complexity Analysis

### 1. LC 121 — Best Time to Buy and Sell Stock
- **Time Complexity:** $O(n)$ — The algorithm performs a single pass over the array of $n$ prices, updating the minimum price and maximum profit at each step in $O(1)$ constant time.
- **Space Complexity:** $O(1)$ — Only two scalar variables (`min_price` and `max_profit`) are used, requiring constant additional memory.

---

### 2. LC 169 — Majority Element
- **Time Complexity:** $O(n)$ — Boyer-Moore Voting Algorithm scans the array of $n$ elements exactly once, updating the candidate and counter in constant time.
- **Space Complexity:** $O(1)$ — The algorithm tracks state using only two primitive variables (`candidate` and `count`), operating without auxiliary collections.

---

### 3. LC 268 — Missing Number
- **Time Complexity:** $O(n)$ — Calculating the array sum requires iterating through $n$ elements once, combined with an $O(1)$ mathematical formula evaluation.
- **Space Complexity:** $O(1)$ — Uses simple mathematical summation variables (`expected_sum` and `actual_sum`) without allocating extra memory structures.

---

### 4. LC 448 — Find All Numbers Disappeared in an Array
- **Time Complexity:** $O(n)$ — Performs two linear passes over the input array: one to negate numbers at corresponding indices and one to collect missing positive index values.
- **Space Complexity:** $O(1)$ auxiliary space — Reuses the input array in-place for state tracking, allocating space only for the required output list.
