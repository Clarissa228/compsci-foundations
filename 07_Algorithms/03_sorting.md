# Sorting Algorithms

## Why Sorting Matters

Sorting is one of the most fundamental operations in CS. Sorted data enables binary search, makes duplicates easy to find, and is required by many algorithms.

There are dozens of sorting algorithms. We'll cover the most important ones — starting simple and working toward efficient.

---

## Bubble Sort — The Simple One

**Idea**: Repeatedly swap adjacent elements if they're in the wrong order. "Bubbles" the largest value to the end on each pass.

```python
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):   # Each pass reduces work by 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]   # Swap

nums = [5, 1, 4, 2, 8]
bubble_sort(nums)
print(nums)   # [1, 2, 4, 5, 8]
```

**Tracing through `[5, 1, 4, 2, 8]`:**
```
Pass 1: [1, 4, 2, 5, 8]  (5 bubbles to end)
Pass 2: [1, 2, 4, 5, 8]  (4 bubbles to near-end)
Pass 3: [1, 2, 4, 5, 8]  (no swaps needed — could stop)
```

**Performance**: O(n²) — very slow for large lists. But simple to understand!

---

## Selection Sort

**Idea**: Find the smallest element and put it at the front. Repeat for the rest.

```python
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]   # Swap minimum to position i
```

**Performance**: O(n²) — same as bubble sort, but does fewer swaps

---

## Insertion Sort

**Idea**: Build a sorted sub-list by inserting each new element in its correct position — like sorting playing cards in your hand.

```python
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]   # Shift right
            j -= 1
        lst[j + 1] = key          # Insert in correct spot
```

**Performance**: O(n²) worst case, but **O(n) on nearly-sorted data** — this makes it very practical for small or nearly-sorted lists.

---

## Merge Sort — The Efficient One

**Idea** (Divide and Conquer):
1. Split the list in half
2. Recursively sort each half
3. Merge the two sorted halves back together

```python
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])    # Sort left half
    right = merge_sort(lst[mid:])   # Sort right half
    return merge(left, right)       # Merge them

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

nums = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(nums))   # [3, 9, 10, 27, 38, 43, 82]
```

**Performance**: O(n log n) — much faster than O(n²) for large lists

---

## Sorting Algorithm Comparison

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Python's `sort()` | O(n) | O(n log n) | O(n log n) | O(n) |

Python's built-in sort uses **Timsort** — a hybrid of merge sort and insertion sort, designed to be fast on real-world data.

---

## Python's Built-in Sorting

You'll rarely need to implement sorting yourself:

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]

# Sort in place
nums.sort()                  # [1, 1, 2, 3, 4, 5, 6, 9]
nums.sort(reverse=True)      # [9, 6, 5, 4, 3, 2, 1, 1]

# Return new sorted list
sorted_nums = sorted(nums)

# Sort by custom key
words = ["banana", "apple", "cherry", "date"]
words.sort(key=len)          # Sort by string length
print(words)   # ['date', 'apple', 'banana', 'cherry']
```

---

## 📺 Watch These

1. **Sorting Algorithms Visualized** — Timo Bingmann (beautiful visualizations!)
   👉 [https://www.youtube.com/watch?v=kPRA0W1kECg](https://www.youtube.com/watch?v=kPRA0W1kECg)

2. **Merge Sort in Python** — CS Dojo
   👉 [https://www.youtube.com/watch?v=cVZMah9kEjI](https://www.youtube.com/watch?v=cVZMah9kEjI)

---

## Key Takeaways

- Bubble, Selection, Insertion sort: simple but O(n²) — fine for small data
- Merge sort: O(n log n) — efficient for large data, uses divide-and-conquer
- In real Python code, use `list.sort()` or `sorted()` — they're fast and reliable
- Understanding these algorithms teaches you to *think* about efficiency

---

*Next up → [Big-O Notation](./04_big_o.md)*
