# Lists

## The Big Idea

A **list** is an ordered collection of items. It's one of Python's most important built-in types — you'll use it constantly.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [42, "hello", True, 3.14]   # Lists can hold any type
empty = []
```

---

## Accessing Items (Indexing)

Items are numbered from **0**:

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # "apple"
print(fruits[1])   # "banana"
print(fruits[2])   # "cherry"
print(fruits[-1])  # "cherry"  (negative: count from end)
print(fruits[-2])  # "banana"
```

---

## Slicing

Get a portion of a list:

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[2:5])    # [2, 3, 4]   (from index 2, up to but not including 5)
print(nums[:4])     # [0, 1, 2, 3]  (from start to index 4)
print(nums[6:])     # [6, 7, 8, 9]  (from index 6 to end)
print(nums[::2])    # [0, 2, 4, 6, 8]  (every 2nd element)
print(nums[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  (reversed!)
```

---

## Modifying Lists

```python
fruits = ["apple", "banana", "cherry"]

# Change an item
fruits[1] = "mango"
print(fruits)   # ["apple", "mango", "cherry"]

# Add items
fruits.append("grape")        # Add to end
fruits.insert(1, "orange")    # Insert at index 1

# Remove items
fruits.remove("mango")        # Remove by value
del fruits[0]                 # Remove by index
popped = fruits.pop()         # Remove & return last item
popped = fruits.pop(1)        # Remove & return item at index 1
```

---

## Useful List Methods

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(numbers))        # 8        — number of items
print(sum(numbers))        # 31       — sum of all items
print(min(numbers))        # 1        — smallest item
print(max(numbers))        # 9        — largest item
print(numbers.count(1))    # 2        — how many times 1 appears
print(numbers.index(5))    # 4        — index of value 5

numbers.sort()             # Sort in place (ascending)
print(numbers)             # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True) # Sort descending
numbers.reverse()          # Reverse in place

sorted_copy = sorted(numbers)  # Returns NEW sorted list, doesn't modify original
```

---

## Looping Over Lists

```python
fruits = ["apple", "banana", "cherry"]

# Basic loop
for fruit in fruits:
    print(fruit)

# With index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Loop over range of indices
for i in range(len(fruits)):
    print(fruits[i])
```

---

## List Comprehensions

A compact way to build lists:

```python
# Without comprehension
squares = []
for i in range(1, 6):
    squares.append(i ** 2)

# With comprehension — cleaner!
squares = [i ** 2 for i in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

# With a condition
evens = [i for i in range(20) if i % 2 == 0]
print(evens)   # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

---

## Checking Membership

```python
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)      # True
print("grape" in fruits)      # False
print("grape" not in fruits)  # True
```

---

## 📺 Watch These

1. **Python Lists** — Corey Schafer
   👉 [https://www.youtube.com/watch?v=W8KRzm-HUcc](https://www.youtube.com/watch?v=W8KRzm-HUcc)

2. **Python List Comprehensions** — Tech With Tim
   👉 [https://www.youtube.com/watch?v=3dt4OGnU5sM](https://www.youtube.com/watch?v=3dt4OGnU5sM)

---

## Key Takeaways

- Lists are **ordered**, **mutable** (changeable), and can hold any type
- Access items with `list[index]` — indices start at **0**
- Slicing `list[start:stop:step]` extracts portions
- `.append()`, `.remove()`, `.pop()`, `.sort()` are the most-used methods
- **List comprehensions** `[expr for x in iterable if condition]` build lists compactly

---

*Next up → [Tuples & Sets](./02_tuples_and_sets.md)*
