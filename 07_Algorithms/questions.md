# Module 7 — Practice Questions

---

## Section A: Searching

1. Implement `linear_search(lst, target)` from scratch (don't look at the notes). Test it on a list with your own values.

2. Implement `binary_search(lst, target)` iteratively. Test it on a sorted list. What happens if you accidentally call it on an *unsorted* list?

3. What is the maximum number of comparisons binary search needs to find an element in a list of:
   - 8 elements
   - 64 elements
   - 1,024 elements
   - 1,048,576 (2²⁰) elements
   (Use the formula: max comparisons ≈ log₂(n) + 1)

4. Write a function `find_all_occurrences(lst, target)` that returns a list of **all** indices where `target` appears (not just the first one). What is the time complexity?

---

## Section B: Sorting

5. Implement **bubble sort** from scratch and trace through `[3, 1, 4, 1, 5]` step by step (show the list after each pass).

6. Implement **insertion sort** from scratch. Test it on both a random list and an already-sorted list.

7. Implement **merge sort** recursively.

8. Given these sort use cases, which algorithm would you choose and why?
   - Sorting 10 items in a user-facing dropdown
   - Sorting 10 million records in a database
   - Sorting a list that's almost entirely sorted already (99% in order)

---

## Section C: Big-O

9. What is the Big-O complexity of each of these code snippets? Explain your reasoning:

   ```python
   # Snippet A
   def f(n):
       total = 0
       for i in range(n):
           total += i
       return total
   ```

   ```python
   # Snippet B
   def g(lst):
       for i in range(len(lst)):
           for j in range(len(lst)):
               if lst[i] == lst[j] and i != j:
                   return True
       return False
   ```

   ```python
   # Snippet C
   def h(n):
       if n <= 1:
           return 1
       return h(n // 2) + 1
   ```

   ```python
   # Snippet D
   def k(lst):
       result = []
       for item in lst:
           result.append(item * 2)
       return result
   ```

10. Rank these from fastest to slowest for n = 10,000:
    - O(n²)
    - O(log n)
    - O(n log n)
    - O(1)
    - O(n)

11. A function takes 1 second for n=100. Estimate how long it takes for n=1000 if:
    - It is O(n)
    - It is O(n²)
    - It is O(log n)

---

## Section D: Algorithm Design

12. **Two Sum**: Given a list of integers and a target, return the indices of two numbers that add up to the target.
    - `two_sum([2, 7, 11, 15], 9)` → `[0, 1]`
    - Write a brute force O(n²) solution
    - Then write an O(n) solution using a dictionary

13. **Reverse a sorted list without using `.reverse()` or slicing**. What is the time complexity?

14. **Count inversions**: An inversion is a pair (i, j) where i < j but lst[i] > lst[j]. Count how many inversions are in `[3, 1, 2]`. Then write a function that counts all inversions in O(n²).

---

## Section E: Challenges

15. **Memoized Fibonacci**: Write a Fibonacci function that uses a dictionary to cache results. Compare its speed to the naive recursive version for `fib(35)` using Python's `time` module.

16. **Binary search variant**: Write a function `find_first(sorted_lst, target)` that returns the index of the **first** occurrence of target in a sorted list (there may be duplicates). Must be O(log n).

17. **Merge sorted lists**: Given two already-sorted lists, merge them into one sorted list *without using sort()*. What is the time complexity?

---

## Answers

<details>
<summary>Q3 — Click to reveal</summary>

- 8 elements: log₂(8) = 3 comparisons
- 64 elements: log₂(64) = 6 comparisons
- 1,024 elements: log₂(1024) = 10 comparisons
- 1,048,576 elements: log₂(1,048,576) = 20 comparisons

This is why binary search is so powerful!

</details>

<details>
<summary>Q9 — Click to reveal</summary>

- Snippet A: **O(n)** — one loop from 0 to n
- Snippet B: **O(n²)** — nested loops, each 0 to n
- Snippet C: **O(log n)** — n is halved each call
- Snippet D: **O(n)** — one loop, constant work per item

</details>

<details>
<summary>Q10 — Click to reveal</summary>

Fastest to slowest: O(1) < O(log n) < O(n) < O(n log n) < O(n²)

</details>

<details>
<summary>Q12 — O(n) hint</summary>

Use a dictionary to store `{value: index}` as you iterate. For each number, check if `target - number` is already in the dictionary.

```python
def two_sum(lst, target):
    seen = {}
    for i, num in enumerate(lst):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

</details>
