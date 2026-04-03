# Module 3 — Practice Questions

Write all answers as runnable Python code. Test each one!

---

## Section A: Conditionals

1. Write a program that asks for a number and prints:
   - "Positive" if greater than 0
   - "Negative" if less than 0
   - "Zero" if equal to 0

2. Write a program that asks for a test score (0–100) and prints the letter grade (A/B/C/D/F).

3. A movie ticket costs:
   - $5 for kids under 12
   - $10 for ages 12–64
   - $7 for seniors 65 and older
   Write a program that asks for age and prints the ticket price.

4. What does this code print? Work it out by hand first:
   ```python
   x = 10
   y = 20
   z = 15

   if x > y:
       print("A")
   elif z > y:
       print("B")
   elif z > x:
       print("C")
   else:
       print("D")
   ```

---

## Section B: Loops

5. Print all numbers from 1 to 50 that are divisible by 7.

6. Write a program that computes the **sum of all integers from 1 to 100** using a loop. (The answer is 5050 — verify yours matches!)

7. Ask the user for a number `n`. Print the **multiplication table** for `n` (1×n through 10×n).

8. Ask the user for a word. Print each letter on its own line, **numbered** starting at 1:
   ```
   1: H
   2: e
   3: l
   4: l
   5: o
   ```

9. Write a program that counts how many **vowels** are in a sentence entered by the user.

---

## Section C: While Loops

10. Write a **number guessing game**:
    - The computer picks a number between 1 and 100 (use `import random; secret = random.randint(1, 100)`)
    - The user keeps guessing until they get it right
    - Print "Too high!", "Too low!", or "Correct!"
    - At the end, print how many guesses it took

11. Write a program that keeps asking the user for numbers and adds them up, **until they type `done`**. Then print the total.

12. Write an input validator: ask for a password. Keep asking until the user types a password that is **at least 8 characters long**. Then print "Password accepted."

---

## Section D: Patterns (Nested Loops)

13. Print this triangle (5 rows):
    ```
    *
    **
    ***
    ****
    *****
    ```

14. Print this **right-aligned** triangle:
    ```
        *
       **
      ***
     ****
    *****
    ```

15. Print a times table grid from 1×1 to 5×5:
    ```
    1  2  3  4  5
    2  4  6  8  10
    3  6  9  12 15
    4  8  12 16 20
    5  10 15 20 25
    ```

---

## Section E: Challenges

16. **FizzBuzz** — Implement the classic FizzBuzz from 1 to 100 (see the notes). Can you do it without looking?

17. **Prime Numbers**: Print all prime numbers between 1 and 50. (A prime number is only divisible by 1 and itself.)

18. **Fibonacci Sequence**: Print the first 15 numbers of the Fibonacci sequence (each number is the sum of the two before it):
    `1, 1, 2, 3, 5, 8, 13, 21, ...`

---

## Answers

<details>
<summary>Q4 — Click to reveal</summary>

The code prints **C**.

- `x > y` → `10 > 20` → False
- `z > y` → `15 > 20` → False
- `z > x` → `15 > 10` → True ✓ → prints "C"

</details>

<details>
<summary>Q6 — Click to reveal</summary>

```python
total = 0
for i in range(1, 101):
    total += i
print(total)  # 5050
```

</details>

<details>
<summary>Q17 — Hint</summary>

For each number `n` from 2 to 50:
- Try dividing it by every number from 2 to n-1
- If none divide evenly, it's prime
- Use a flag variable `is_prime = True` and set it to `False` if you find a divisor

</details>
