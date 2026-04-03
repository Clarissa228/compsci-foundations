# Tuples & Sets

---

## Tuples

A **tuple** is like a list, but **immutable** — once created, it cannot be changed.

```python
point = (3, 7)
rgb = (255, 128, 0)
person = ("Alice", 17, "New York")
```

### Accessing Tuple Items

Just like lists:
```python
person = ("Alice", 17, "New York")
print(person[0])    # "Alice"
print(person[-1])   # "New York"
```

### Unpacking Tuples

A key feature — you can unpack a tuple into separate variables:
```python
name, age, city = ("Alice", 17, "New York")
print(name)   # Alice
print(age)    # 17
```

You've already seen this with `enumerate()` and `min_max()` functions that return multiple values.

### When to Use Tuples

- When data **should not change** (coordinates, RGB colors, database rows)
- When returning multiple values from a function
- As dictionary keys (lists can't be used as keys, but tuples can!)

```python
# Tuple as dict key
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}
```

---

## Sets

A **set** is an **unordered** collection with **no duplicate values**.

```python
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)   # {"apple", "banana", "cherry"} — duplicates removed automatically
```

### Modifying Sets

```python
fruits = {"apple", "banana"}

fruits.add("cherry")        # Add one item
fruits.update(["mango", "grape"])  # Add multiple items
fruits.remove("banana")     # Remove (raises error if not found)
fruits.discard("kiwi")      # Remove (no error if not found)
```

### Set Operations — Extremely Useful

Sets support mathematical set operations:

```python
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a | b)    # Union: {1, 2, 3, 4, 5, 6, 7}       — all items from both
print(a & b)    # Intersection: {3, 4, 5}             — items in both
print(a - b)    # Difference: {1, 2}                  — items in a but not b
print(a ^ b)    # Symmetric difference: {1, 2, 6, 7}  — items in one but not both
```

### Fast Membership Testing

Sets check if something is in them **much faster** than lists (we'll understand why in Module 8):

```python
big_list = list(range(1_000_000))
big_set = set(range(1_000_000))

# Both work, but set is far faster
print(999999 in big_list)   # Slow
print(999999 in big_set)    # Very fast
```

### Common Use: Removing Duplicates

```python
numbers = [1, 3, 2, 3, 1, 4, 2, 5]
unique = list(set(numbers))
print(unique)   # [1, 2, 3, 4, 5]  (order not guaranteed)
```

---

## Comparison: List vs Tuple vs Set

| Feature | List | Tuple | Set |
|---------|------|-------|-----|
| Ordered | ✅ | ✅ | ❌ |
| Mutable | ✅ | ❌ | ✅ |
| Allows duplicates | ✅ | ✅ | ❌ |
| Use `[]` | ✅ | `()` | `{}` |
| Best for | General sequences | Fixed data, multiple returns | Uniqueness, fast lookup |

---

## 📺 Watch These

1. **Python Tuples** — Corey Schafer
   👉 [https://www.youtube.com/watch?v=NI26dqhs2Rk](https://www.youtube.com/watch?v=NI26dqhs2Rk)

2. **Python Sets** — Corey Schafer
   👉 [https://www.youtube.com/watch?v=r3R3h5ly_8g](https://www.youtube.com/watch?v=r3R3h5ly_8g)

---

## Key Takeaways

- **Tuples**: ordered, immutable, allow duplicates — great for fixed data and multiple returns
- **Sets**: unordered, mutable, **no duplicates** — great for uniqueness and fast lookup
- Set operations (`|`, `&`, `-`, `^`) are powerful for comparing collections
- `list(set(my_list))` is a quick way to remove duplicates from a list

---

*Next up → [Dictionaries](./03_dictionaries.md)*
