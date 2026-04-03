# Nested Logic & Combining Control Flow

## The Big Idea

Real programs combine conditionals and loops together. Understanding how to nest them and read complex logic is a key skill that separates beginners from intermediate programmers.

---

## Loops + Conditionals Together

One of the most common patterns: loop through data and check conditions inside:

```python
numbers = [3, 7, 12, 4, 9, 18, 2, 15]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
```

---

## Accumulating Results

A classic pattern: use a variable to track a running total:

```python
scores = [82, 91, 78, 95, 67, 88]

total = 0
for score in scores:
    total += score

average = total / len(scores)
print(f"Average score: {average:.1f}")
```

---

## Finding Items with Loops

```python
names = ["Alice", "Bob", "Charlie", "Diana"]
search = input("Search for a name: ")

found = False
for name in names:
    if name.lower() == search.lower():
        found = True
        break

if found:
    print(f"Found {search}!")
else:
    print(f"{search} not found.")
```

---

## While Loop with User Input Validation

A very practical pattern — keep asking until the user gives valid input:

```python
while True:
    age = input("Enter your age (must be positive): ")

    if age.isdigit() and int(age) > 0:
        age = int(age)
        break
    else:
        print("Invalid input. Try again.")

print(f"Your age is {age}.")
```

---

## The `for/else` and `while/else` Pattern

Python has a unique feature: loops can have an `else` clause that runs **only if the loop completed without hitting a `break`**:

```python
numbers = [3, 7, 11, 15, 22, 9]

for num in numbers:
    if num % 2 == 0:
        print(f"First even number found: {num}")
        break
else:
    print("No even numbers in the list")
```

This is handy for search operations.

---

## Pattern Printing (Classic Beginner Exercise)

These exercises are designed to train your loop + nested loop skills:

**Triangle:**
```python
rows = 5
for i in range(1, rows + 1):
    print("*" * i)
```
Output:
```
*
**
***
****
*****
```

**Number pyramid:**
```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```
Output:
```
1
12
123
1234
12345
```

---

## Fizzbuzz — A Famous Interview Problem

Print numbers 1 to 100. But:
- For multiples of 3, print "Fizz"
- For multiples of 5, print "Buzz"
- For multiples of both 3 and 5, print "FizzBuzz"

```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

> Why check `i % 15` first? Because if you check `i % 3` first, "FizzBuzz" numbers would match that case and never reach the FizzBuzz check.

---

## 📺 Watch These

1. **Python FizzBuzz Explained** — CS Dojo
   👉 [https://www.youtube.com/watch?v=A3GxAS4BnOI](https://www.youtube.com/watch?v=A3GxAS4BnOI)

2. **Python Control Flow Deep Dive** — Real Python
   👉 [https://www.youtube.com/watch?v=Zp5MuPOtsSY](https://www.youtube.com/watch?v=Zp5MuPOtsSY)

---

## Key Takeaways

- Combine loops and conditionals to process collections of data
- Use accumulator variables (`total = 0`) to track running results
- `while True: ... break` is the cleanest pattern for input validation
- FizzBuzz is a classic problem — make sure you can solve it from scratch
- Nested loops are powerful but hard to read — keep nesting to 2 levels if possible

---

*Next up → [Practice Questions](./questions.md)*
