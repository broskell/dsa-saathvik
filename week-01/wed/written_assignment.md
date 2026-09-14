# Assignment 1.2 Written Question

**Question:** Why is `x in set` faster than `x in list`? Write three sentences explaining why.

**Answer:**
Checking `x in list` requires a linear search ($O(n)$ time complexity) because elements are stored sequentially in memory and must be compared one by one from the beginning until a match is found or the end is reached. In contrast, `x in set` uses a hash table mechanism where the element's hash value directly maps to a specific bucket index, allowing membership checks in $O(1)$ constant time on average regardless of the collection size. Consequently, as the dataset grows into thousands or millions of items, set lookups remain virtually instantaneous while list searches become drastically slower by multiple orders of magnitude.
