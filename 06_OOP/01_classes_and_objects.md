# Classes & Objects

## The Big Idea

**Object-Oriented Programming (OOP)** is a way of organizing code by modeling real-world things as **objects**. An object bundles together both *data* (attributes) and *behavior* (methods).

A **class** is a blueprint. An **object** is an instance created from that blueprint.

Think of it like this:
- **Class** = the blueprint for a house
- **Object** = an actual house built from that blueprint

---

## Your First Class

```python
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof!")

    def describe(self):
        print(f"{self.name} is a {self.age}-year-old {self.breed}.")
```

Breaking it down:
- `class Dog:` — defines the class
- `__init__` — the **constructor**: runs automatically when an object is created
- `self` — refers to the specific object instance (like "this" in other languages)
- `self.name = name` — stores `name` as an **attribute** of this object

---

## Creating Objects (Instances)

```python
dog1 = Dog("Buddy", "Labrador", 3)
dog2 = Dog("Max", "Poodle", 5)

dog1.bark()       # Buddy says: Woof!
dog2.describe()   # Max is a 5-year-old Poodle.

print(dog1.name)  # Buddy
print(dog2.age)   # 5
```

Each object has its own copy of the attributes.

---

## Instance vs Class Attributes

**Instance attributes** belong to a specific object:
```python
dog1.name = "Buddy"   # Only this dog has this name
```

**Class attributes** are shared across all instances:
```python
class Dog:
    species = "Canis lupus familiaris"   # Shared by all dogs

    def __init__(self, name):
        self.name = name

print(Dog.species)      # Canis lupus familiaris
print(dog1.species)     # Canis lupus familiaris — also accessible from instance
```

---

## A More Complete Example

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def __str__(self):
        return f"Account({self.owner}, ${self.balance})"


account = BankAccount("Alice", 1000)
account.deposit(500)        # Deposited $500. New balance: $1500
account.withdraw(200)       # Withdrew $200. New balance: $1300
print(account)              # Account(Alice, $1300)
```

The `__str__` method defines how the object prints — called a **dunder** (double underscore) method.

---

## 📺 Watch These

1. **Python OOP Tutorial** — Corey Schafer (6-part series)
   👉 [https://www.youtube.com/watch?v=ZDa-Z5JzLYM](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)

2. **Object-Oriented Programming in 7 Minutes** — Programming with Mosh
   👉 [https://www.youtube.com/watch?v=pTB0EiLXUC8](https://www.youtube.com/watch?v=pTB0EiLXUC8)

---

## Key Takeaways

- A **class** is a blueprint; an **object** is an instance of that class
- `__init__` is the constructor — runs when you create an object
- `self` refers to the specific object instance
- **Attributes** store data; **methods** define behavior
- `__str__` controls how an object looks when printed

---

*Next up → [Inheritance](./02_inheritance.md)*
