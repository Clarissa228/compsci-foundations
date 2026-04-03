# Dictionaries

## The Big Idea

A **dictionary** (dict) stores **key-value pairs** — like a real dictionary where you look up a word (the key) to find its definition (the value).

```python
student = {
    "name": "Alice",
    "age": 17,
    "grade": "A"
}
```

Dictionaries are incredibly useful for representing real-world objects.

---

## Creating Dictionaries

```python
# Literal syntax
person = {"name": "Bob", "age": 25}

# Empty dict
empty = {}

# Using dict()
config = dict(host="localhost", port=8080)
```

---

## Accessing Values

```python
student = {"name": "Alice", "age": 17, "grade": "A"}

print(student["name"])          # "Alice"
print(student.get("age"))       # 17
print(student.get("email"))     # None (doesn't raise an error)
print(student.get("email", "N/A"))  # "N/A" (default value)
```

> ⚠️ `student["email"]` would raise a `KeyError` if the key doesn't exist. Use `.get()` to avoid this.

---

## Modifying Dictionaries

```python
student = {"name": "Alice", "age": 17}

# Add or update
student["grade"] = "A"         # Add new key
student["age"] = 18            # Update existing key

# Remove
del student["grade"]           # Delete by key
removed = student.pop("age")   # Remove and return the value

print(student)   # {"name": "Alice"}
```

---

## Looping Over Dictionaries

```python
person = {"name": "Alice", "age": 17, "city": "NYC"}

# Loop over keys (default)
for key in person:
    print(key)

# Loop over values
for value in person.values():
    print(value)

# Loop over key-value pairs (most common)
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## Useful Dictionary Methods

```python
d = {"a": 1, "b": 2, "c": 3}

print(d.keys())     # dict_keys(['a', 'b', 'c'])
print(d.values())   # dict_values([1, 2, 3])
print(d.items())    # dict_items([('a', 1), ('b', 2), ('c', 3)])

# Check if key exists
print("a" in d)     # True
print("z" in d)     # False

# Merge two dicts (Python 3.9+)
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2   # {"a": 1, "b": 2}
```

---

## Dictionary Comprehensions

```python
# Square each number
squares = {i: i**2 for i in range(1, 6)}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter — only even squares
even_squares = {i: i**2 for i in range(1, 11) if i % 2 == 0}
```

---

## Nested Dictionaries

Real-world data is often nested:

```python
users = {
    "alice": {"age": 17, "email": "alice@example.com"},
    "bob":   {"age": 22, "email": "bob@example.com"}
}

print(users["alice"]["email"])   # alice@example.com

# Add a new user
users["carol"] = {"age": 19, "email": "carol@example.com"}
```

---

## Counting with Dictionaries

A very common pattern:

```python
sentence = "hello world hello python"
word_count = {}

for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
# {'hello': 2, 'world': 1, 'python': 1}
```

Or using `collections.Counter`:
```python
from collections import Counter
word_count = Counter(sentence.split())
```

---

## 📺 Watch These

1. **Python Dictionaries** — Corey Schafer
   👉 [https://www.youtube.com/watch?v=daefaLgNkw0](https://www.youtube.com/watch?v=daefaLgNkw0)

2. **Python Dictionary Methods** — Tech With Tim
   👉 [https://www.youtube.com/watch?v=XCcpzWs-CI4](https://www.youtube.com/watch?v=XCcpzWs-CI4)

---

## Key Takeaways

- Dictionaries store **key-value pairs** — look up any value instantly by key
- Use `.get(key, default)` for safe access without errors
- `.keys()`, `.values()`, `.items()` let you loop over different parts
- Dictionary comprehensions build dicts compactly
- Counting occurrences with dicts is a super common coding pattern

---

*Next up → [Strings Deep Dive](./04_strings.md)*
