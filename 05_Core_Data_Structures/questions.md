# Module 5 — Practice Questions

---

## Section A: Lists

1. Given `nums = [5, 2, 8, 1, 9, 3, 7]`:
   - Print the first 3 elements
   - Print the last 2 elements
   - Print the list in reverse
   - Print only the elements at even indices (0, 2, 4, 6)

2. Write a function `second_largest(lst)` that returns the second largest number in a list *without sorting it*. (Hint: track largest and second largest in one pass.)

3. Write a function `remove_duplicates(lst)` that returns a new list with duplicates removed, **preserving order** (so `[1, 3, 2, 3, 1]` → `[1, 3, 2]`). Don't use a set directly — use a loop.

4. Use a list comprehension to create a list of all numbers from 1 to 30 that are divisible by 3 **or** end in the digit 7.

5. Write a function `flatten_once(lst)` that flattens one level of nesting:
   `[[1,2], [3,4], [5,6]]` → `[1, 2, 3, 4, 5, 6]`
   Use a list comprehension.

---

## Section B: Tuples & Sets

6. Create a tuple `coordinates = (40.7128, -74.0060)` representing a GPS location. Unpack it into two variables `lat` and `lon` and print them with labels.

7. Given two lists of student names — one from class A and one from class B — find:
   - Students in **both** classes (intersection)
   - Students in **either** class (union)
   - Students **only** in class A (difference)

   Use sets.

8. Write a function `all_unique(lst)` that returns `True` if all elements in a list are unique, `False` otherwise. Use a set.

9. What's the difference between `(1)` and `(1,)` in Python? Try both in the interpreter and explain.

---

## Section C: Dictionaries

10. Create a phone book dictionary with at least 4 entries (name → phone number). Write a lookup program that asks the user for a name and prints the number, or "Not found" if the name isn't in the book.

11. Write a function `letter_frequency(text)` that returns a dictionary mapping each letter to how many times it appears in the text (ignore spaces and punctuation, case-insensitive).

12. You have a list of student scores:
    ```python
    scores = [("Alice", 92), ("Bob", 78), ("Carol", 85), ("Dave", 92), ("Eve", 78)]
    ```
    Convert this to a dictionary where each score maps to a list of students who earned it:
    `{92: ["Alice", "Dave"], 78: ["Bob", "Eve"], 85: ["Carol"]}`

13. Write a function `invert_dict(d)` that swaps keys and values:
    `{"a": 1, "b": 2, "c": 3}` → `{1: "a", 2: "b", 3: "c"}`

---

## Section D: Strings

14. Write a function `is_palindrome(s)` that returns `True` if a string reads the same forwards and backwards (ignore case and spaces):
    - `"racecar"` → True
    - `"A man a plan a canal Panama"` → True (after removing spaces)

15. Write a function `title_case(sentence)` that capitalizes the first letter of every word, but **without** using `.title()`. Use `.split()` and `.join()`.

16. Write a function `count_words(text)` that returns a dictionary of word counts. Ignore punctuation (hint: `word.strip(".,!?;:")`) and treat everything as lowercase.

17. Write a Caesar cipher encoder:
    - `encode(text, shift)` shifts every letter by `shift` positions
    - `encode("hello", 3)` → `"khoor"`
    - Hint: use `ord()` to get the ASCII value of a character, and `chr()` to convert back

---

## Section E: Challenges

18. **Anagram checker**: Write a function `are_anagrams(s1, s2)` that returns `True` if the two strings are anagrams (contain the same letters, same frequency):
    - `"listen"`, `"silent"` → True
    - `"hello"`, `"world"` → False

19. **Top N words**: Write a function `top_n_words(text, n)` that returns the `n` most common words in a text.

20. **Matrix transpose**: Given a 2D list (list of lists) representing a matrix, return its transpose:
    ```python
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    transpose → [[1,4,7],[2,5,8],[3,6,9]]
    ```
    Write it with a list comprehension.

---

## Answers

<details>
<summary>Q9 — Click to reveal</summary>

`(1)` is just the integer `1` in parentheses. Python sees the parentheses as grouping, not a tuple.
`(1,)` is a tuple with one element — the trailing comma is what makes it a tuple.

```python
print(type((1)))   # <class 'int'>
print(type((1,)))  # <class 'tuple'>
```

</details>

<details>
<summary>Q14 hint</summary>

```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
```

</details>

<details>
<summary>Q17 hint</summary>

```python
def encode(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result
```

</details>
