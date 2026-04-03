# Module 6 — Practice Questions

---

## Section A: Classes & Objects

1. Create a `Rectangle` class with:
   - `__init__(width, height)`
   - `area()` method → returns width × height
   - `perimeter()` method → returns 2 × (width + height)
   - `is_square()` method → returns True if width == height
   - `__str__` → prints `"Rectangle(4 x 6)"`

2. Create a `Student` class with:
   - `name`, `grades` (list of numbers) as attributes
   - `add_grade(score)` method
   - `average()` method → returns average of grades
   - `highest()` and `lowest()` methods
   - `__str__` → prints student name and average

3. Create a `Counter` class that:
   - Starts at 0
   - Has `increment()`, `decrement()`, `reset()` methods
   - Has a `value` property (read-only — using `@property`)
   - Prevents the counter from going below 0

---

## Section B: Inheritance

4. Create a base class `Vehicle` with attributes `make`, `model`, `year` and a method `describe()`. Then create:
   - `Car(Vehicle)` — adds `num_doors` attribute
   - `Motorcycle(Vehicle)` — adds `has_sidecar` attribute
   Each subclass should call `super().__init__()` and override `describe()` with more detail.

5. Create a class hierarchy for shapes:
   - `Shape` base class with an `area()` method that returns 0
   - `Circle(Shape)` — override `area()`
   - `Rectangle(Shape)` — override `area()`
   - `Triangle(Shape)` — override `area()` (use base × height / 2)

   Then write a function `total_area(shapes)` that takes a list of any shapes and returns the sum of their areas.

6. Create a `Person` base class and `Employee(Person)` subclass:
   - `Person`: name, age
   - `Employee`: adds company, salary, and a `give_raise(percent)` method

---

## Section C: Encapsulation

7. Rewrite the `BankAccount` class from the notes using:
   - A `_balance` private attribute
   - `deposit()` and `withdraw()` with validation
   - A `balance` property (read-only — no setter)
   - `__str__`

8. Create a `Password` class that:
   - Stores a password (minimum 8 characters) — raise `ValueError` if too short
   - Has a `value` property that **never reveals the real password** (returns `"****"` instead)
   - Has a `check(attempt)` method that returns `True` if the attempt matches

9. Create a `Thermostat` class with:
   - A `temperature` property in Celsius
   - A setter that rejects temperatures below -10 or above 40 (valid room temperatures)
   - A read-only `fahrenheit` property derived from celsius

---

## Section D: Dunder Methods

10. Create a `Fraction` class that represents a fraction (numerator/denominator). Implement:
    - `__str__` → `"3/4"`
    - `__add__` → adds two fractions correctly using cross-multiplication
    - `__mul__` → multiplies two fractions
    - `__eq__` → checks if two fractions are equal (after simplification)
    - Bonus: simplify fractions automatically using GCD

11. Create a `Matrix` class for a 2x2 matrix. Implement:
    - `__init__(a, b, c, d)` — stores `[[a,b],[c,d]]`
    - `__add__` — element-wise addition
    - `__mul__` — matrix multiplication
    - `__str__` — prints as a grid

---

## Section E: Challenge

12. **RPG Character System**: Design a mini RPG (role-playing game) character system:
    - `Character` base class with `name`, `hp`, `max_hp`, `attack_power`
    - Methods: `take_damage(amount)`, `heal(amount)`, `is_alive()`, `__str__`
    - `Warrior(Character)` — bonus armor that reduces damage by 2
    - `Mage(Character)` — can cast a spell that deals double damage but costs 10 HP
    - Write a simple combat simulator that pits a Warrior against a Mage in turns

---

## Answers

<details>
<summary>Q1 — Starting code</summary>

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"
```

</details>

<details>
<summary>Q10 — GCD hint</summary>

```python
from math import gcd

class Fraction:
    def __init__(self, num, den):
        common = gcd(abs(num), abs(den))
        self.num = num // common
        self.den = den // common

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
```

</details>
