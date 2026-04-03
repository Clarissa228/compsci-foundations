# Module 4 — Practice Questions

---

## Section A: Defining Functions

1. Write a function `greet(name)` that returns the string `"Hello, [name]!"` (don't print inside — return it). Then call it and print the result.

2. Write a function `celsius_to_fahrenheit(c)` that converts Celsius to Fahrenheit and returns the result.

3. Write a function `is_even(n)` that returns `True` if `n` is even, `False` otherwise.

4. Write a function `clamp(value, min_val, max_val)` that:
   - Returns `min_val` if `value < min_val`
   - Returns `max_val` if `value > max_val`
   - Returns `value` otherwise

   Test it with: `clamp(5, 0, 10)` → 5, `clamp(-3, 0, 10)` → 0, `clamp(15, 0, 10)` → 10

---

## Section B: Scope

5. What does this code print? Work it out first, then run it:
   ```python
   x = "global"

   def foo():
       x = "local"
       print(x)

   foo()
   print(x)
   ```

6. Fix this code so that `counter` increments correctly:
   ```python
   counter = 0

   def increment():
       counter += 1

   increment()
   increment()
   print(counter)  # Should print 2
   ```

7. Rewrite the above fix *without* using the `global` keyword. (Hint: use a parameter and return value.)

---

## Section C: Return Values

8. Write a function `stats(numbers)` that takes a list of numbers and returns **three values**: the minimum, maximum, and average. Call it and unpack all three:
   ```python
   lo, hi, avg = stats([3, 7, 1, 9, 4])
   ```

9. Write a function `grade(score)` that returns the letter grade for a score (A/B/C/D/F). Use this in a program that reads scores from a list and prints each with its grade.

10. Write a function `count_vowels(text)` that returns the number of vowels in a string.

---

## Section D: Recursion

11. Write a recursive function `sum_up_to(n)` that returns the sum of all integers from 1 to `n`.
    - `sum_up_to(5)` should return `15` (1+2+3+4+5)
    - Make sure to identify the base case first

12. Write a recursive function `power(base, exp)` that calculates `base^exp` without using `**`.
    - `power(2, 10)` → 1024
    - Hint: `2^10 = 2 × 2^9`

13. Write a recursive function `reverse_string(s)` that returns the string in reverse.
    - `reverse_string("hello")` → `"olleh"`
    - Hint: the reverse of "hello" = "o" + reverse("hell")

14. Write a recursive function `count_down(n)` that prints each number from `n` down to 1, then prints "Blast off!". No loops allowed.

---

## Section E: Challenges

15. **Pascal's Triangle row**: Write a function `pascal_row(n)` that returns the nth row of Pascal's Triangle as a list. (Row 0 = [1], Row 1 = [1,1], Row 2 = [1,2,1], etc.)

16. **Flattening**: Write a recursive function `flatten(lst)` that takes a nested list and returns a flat list:
    ```python
    flatten([1, [2, 3], [4, [5, 6]]]) → [1, 2, 3, 4, 5, 6]
    ```

17. **Memoized Fibonacci**: The simple recursive Fibonacci is slow. Rewrite it using a dictionary to cache previously computed values (this technique is called **memoization**):
    ```python
    memo = {}
    def fib_memo(n):
        # Check if already computed, store result before returning
    ```
    Test: `fib_memo(40)` should return almost instantly.

---

## Answers

<details>
<summary>Q5 — Click to reveal</summary>

```
local    ← from inside foo(), where x is "local"
global   ← from outside foo(), where x is "global"
```
The function's local `x` doesn't affect the global `x`.

</details>

<details>
<summary>Q11 — Click to reveal</summary>

```python
def sum_up_to(n):
    if n == 1:      # Base case
        return 1
    return n + sum_up_to(n - 1)   # Recursive case
```

</details>

<details>
<summary>Q13 hint</summary>

```python
def reverse_string(s):
    if len(s) == 0:    # Base case: empty string reverses to ""
        return ""
    return s[-1] + reverse_string(s[:-1])  # Last char + reverse of rest
```

</details>
