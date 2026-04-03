# Module 2 — Practice Questions

Write your answers as actual Python code in a file called `module2_practice.py`. Run each one and check the output.

---

## Section A: Variables & Data Types

1. Create variables for the following and print each one with a descriptive label:
   - Your name (string)
   - Your age (integer)
   - Your GPA or a grade (float)
   - Whether you enjoy coding (boolean)

2. Write code that asks the user for their name and age, then prints:
   ```
   Hello, [name]! You are [age] years old.
   ```

3. What does this code print? Work it out *by hand* first, then run it to check:
   ```python
   x = "5"
   y = 3
   print(x * y)
   ```

4. Fix this broken code (it has type errors):
   ```python
   age = input("Enter your age: ")
   next_year_age = age + 1
   print(f"Next year you will be {next_year_age}")
   ```

---

## Section B: Operators

5. Without running it, predict the output of each line. Then verify in Python:
   ```python
   print(17 % 5)
   print(20 // 3)
   print(2 ** 8)
   print(15 % 2 == 0)
   print(7 > 3 and 10 < 5)
   print(7 > 3 or 10 < 5)
   ```

6. Write a program that:
   - Asks the user to enter a number
   - Prints whether the number is **even** or **odd**
   - (Hint: use the `%` operator)

7. Write a program that converts a temperature from **Celsius to Fahrenheit**:
   - Formula: `F = (C × 9/5) + 32`
   - Ask the user for the Celsius temperature
   - Print the result formatted to 2 decimal places

---

## Section C: Input & Output

8. Write a program that asks for the user's **first name** and **last name** separately, then prints them combined with a space:
   ```
   Full name: Alice Smith
   ```

9. Create a "Mad Libs" style program:
   - Ask for: a noun, a verb, an adjective, and a number
   - Insert them into a funny sentence and print it

10. What does the following print? Work it out before running:
    ```python
    print("*" * 5)
    print("ab" * 3)
    print(f"{'hello':>10}")
    ```

---

## Section D: Challenges

11. **BMI Calculator**: Ask for weight (kg) and height (m). Calculate BMI using:
    `BMI = weight / height²`
    Print the result rounded to 1 decimal place.

12. **Tip Calculator**: Ask for a restaurant bill amount and a tip percentage. Calculate and print:
    - Tip amount
    - Total bill
    - Amount each person pays (ask how many people)

13. **Seconds Converter**: Ask the user for a number of seconds. Convert and print it as:
    ```
    X hours, Y minutes, Z seconds
    ```
    (Hint: use `//` and `%`)

---

## Section E: Reflection

14. What is the difference between `=` and `==` in Python? Give an example of each.

15. Why does `input()` always return a string? Why does this matter?

---

## Answers

<details>
<summary>Section B, Q5 — Click to reveal</summary>

```
17 % 5 → 2
20 // 3 → 6
2 ** 8 → 256
15 % 2 == 0 → False  (15 is odd)
7 > 3 and 10 < 5 → False  (second part is False)
7 > 3 or 10 < 5 → True   (first part is True)
```

</details>

<details>
<summary>Section C, Q10 — Click to reveal</summary>

```
*****
ababab
     hello    (right-aligned in a field of 10 characters)
```

</details>
