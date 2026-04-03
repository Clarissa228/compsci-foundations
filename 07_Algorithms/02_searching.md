# Searching Algorithms

---

## Linear Search

**Idea**: Check each element one by one until you find the target.

```python
def linear_search(lst, target):
    for i, item in enumerate(lst):
        if item == target:
            return i   # Return the index
    return -1          # Return -1 if not found

nums = [4, 2, 9, 7, 5, 1, 8]
print(linear_search(nums, 7))   # 3
print(linear_search(nums, 10))  # -1
```

**Performance**:
- Best case: target is first → 1 check
- Worst case: target is last (or missing) → n checks
- Works on **unsorted or sorted** lists

---

## Binary Search

**Idea**: Only works on a **sorted** list. Repeatedly cut the search space in half.

1. Look at the middle element
2. If it's the target → done
3. If the target is smaller → search the left half
4. If the target is larger → search the right half
5. Repeat until found or the search space is empty

```python
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1    # Target is in right half
        else:
            right = mid - 1   # Target is in left half

    return -1


sorted_nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(sorted_nums, 13))   # 6
print(binary_search(sorted_nums, 6))    # -1
```

### Tracing Through an Example

Searching for `13` in `[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]`:

```
Step 1: left=0, right=9, mid=4 → lst[4]=9  → 9 < 13 → left = 5
Step 2: left=5, right=9, mid=7 → lst[7]=15 → 15 > 13 → right = 6
Step 3: left=5, right=6, mid=5 → lst[5]=11 → 11 < 13 → left = 6
Step 4: left=6, right=6, mid=6 → lst[6]=13 → FOUND at index 6!
```

4 steps to find an element in a 10-element list. Linear would take up to 10.

---

## Binary Search — Recursive Version

```python
def binary_search_recursive(lst, target, left=0, right=None):
    if right is None:
        right = len(lst) - 1

    if left > right:
        return -1   # Base case: not found

    mid = (left + right) // 2

    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        return binary_search_recursive(lst, target, mid + 1, right)
    else:
        return binary_search_recursive(lst, target, left, mid - 1)
```

---

## Comparing the Two

| | Linear Search | Binary Search |
|--|--------------|--------------|
| Requires sorted list? | No | Yes |
| Best case | O(1) | O(1) |
| Worst case | O(n) | O(log n) |
| 1,000 elements, worst case | 1,000 checks | ~10 checks |
| 1,000,000 elements, worst case | 1,000,000 checks | ~20 checks |

(We'll fully explain O(n) and O(log n) in the next topic!)

---

## Python's Built-in Search

Python has built-in tools so you don't always need to implement these:

```python
nums = [4, 2, 9, 7, 5]

# Linear search equivalents
print(7 in nums)          # True (uses linear search internally)
print(nums.index(7))      # 3

# Binary search (for sorted lists) — from standard library
import bisect
sorted_nums = [1, 3, 5, 7, 9, 11]
pos = bisect.bisect_left(sorted_nums, 7)   # Finds insertion point
print(pos)  # 3
```

---

## 📺 Watch These

1. **Binary Search** — CS50 Harvard
   👉 [https://www.youtube.com/watch?v=D5SrAga1pno](https://www.youtube.com/watch?v=D5SrAga1pno)

2. **Linear vs Binary Search** — CS Dojo
   👉 [https://www.youtube.com/watch?v=MFhxShGxHWc](https://www.youtube.com/watch?v=MFhxShGxHWc)

---

## Key Takeaways

- **Linear search**: simple, works anywhere, O(n) worst case
- **Binary search**: fast, requires sorted input, O(log n) worst case
- Binary search is exponentially faster for large data sets
- Real programs often use Python's built-in `in`, `.index()`, or `bisect` module

---

*Next up → [Sorting Algorithms](./03_sorting.md)*
