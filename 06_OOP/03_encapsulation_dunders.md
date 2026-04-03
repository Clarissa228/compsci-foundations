# Encapsulation & Dunder Methods

---

## Encapsulation

**Encapsulation** means hiding an object's internal data from the outside world and controlling access through methods.

### Why Encapsulate?

Without encapsulation, anyone can modify an object's data in unexpected ways:

```python
account = BankAccount("Alice", 1000)
account.balance = -99999999   # 😱 No check, no rules!
```

With encapsulation, you control how data is accessed and changed.

---

## Private Attributes (Convention)

Python uses naming conventions to signal that attributes are "private":

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance      # Single _ = "please don't touch directly"

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Invalid withdrawal amount!")
```

A single underscore `_name` is a convention meaning "this is internal — use the methods instead."

A double underscore `__name` triggers **name mangling** — Python renames it to make it harder to access from outside:
```python
class Foo:
    def __init__(self):
        self.__secret = 42   # Stored as _Foo__secret

foo = Foo()
print(foo._Foo__secret)   # Still accessible, just harder
```

---

## Properties (Pythonic Encapsulation)

Python's `@property` decorator lets you define "getters" and "setters" cleanly:

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32


temp = Temperature(25)
print(temp.celsius)      # 25   — looks like attribute access, runs getter
print(temp.fahrenheit)   # 77.0
temp.celsius = 100       # Runs setter with validation
temp.celsius = -300      # Raises ValueError!
```

---

## Dunder Methods (Magic Methods)

**Dunder** (double underscore) methods let you define how Python's built-in operations work on your objects.

### Common Dunders

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):
        return 2   # 2D vector always has 2 components

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1)           # Vector(1, 2)        ← __str__
print(v1 + v2)      # Vector(4, 6)        ← __add__
print(len(v1))      # 2                   ← __len__
print(v1 == v1)     # True                ← __eq__
```

### Key Dunders to Know

| Method | Triggered by | Description |
|--------|-------------|-------------|
| `__init__` | `MyClass()` | Constructor |
| `__str__` | `print(obj)` | Human-readable string |
| `__repr__` | `repr(obj)` | Developer-readable string |
| `__len__` | `len(obj)` | Length |
| `__add__` | `obj + other` | Addition |
| `__eq__` | `obj == other` | Equality |
| `__lt__` | `obj < other` | Less-than comparison |
| `__getitem__` | `obj[key]` | Indexing |
| `__contains__` | `x in obj` | Membership test |

---

## 📺 Watch These

1. **Python Encapsulation** — Corey Schafer
   👉 [https://www.youtube.com/watch?v=jCzT9XFZ5bw](https://www.youtube.com/watch?v=jCzT9XFZ5bw)

2. **Python Dunder/Magic Methods** — Tech With Tim
   👉 [https://www.youtube.com/watch?v=z11P9sojHuM](https://www.youtube.com/watch?v=z11P9sojHuM)

---

## Key Takeaways

- **Encapsulation** hides internal data and exposes controlled access via methods
- `_name` = convention for "internal"; `__name` = name mangling (harder to access)
- `@property` makes getter/setter logic look like attribute access — very Pythonic
- **Dunder methods** let you define how operators (`+`, `==`, `len()`) work on your class
- Implementing `__str__` makes your objects readable when printed

---

*Next up → [Practice Questions](./questions.md)*
