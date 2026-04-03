# Inheritance & Polymorphism

## Inheritance — The Big Idea

**Inheritance** lets one class *inherit* attributes and methods from another. This promotes code reuse — you define common behavior once in a **parent class** and extend it in **child classes**.

Think of it like genetics: a `Dog` and a `Cat` both inherit from `Animal` (they both have names, ages, and can eat). But they each also have their own unique behaviors.

---

## Basic Inheritance

```python
# Parent class (also called base class or superclass)
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def describe(self):
        print(f"{self.name}, age {self.age}")


# Child class (also called subclass or derived class)
class Dog(Animal):    # Dog inherits from Animal
    def bark(self):
        print(f"{self.name} says: Woof!")


class Cat(Animal):    # Cat inherits from Animal
    def meow(self):
        print(f"{self.name} says: Meow!")


dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 5)

dog.eat()       # Buddy is eating.   ← inherited from Animal
dog.bark()      # Buddy says: Woof!  ← defined in Dog
cat.describe()  # Whiskers, age 5   ← inherited from Animal
cat.meow()      # Whiskers says: Meow!
```

---

## Overriding Methods

A child class can **override** a parent method to change its behavior:

```python
class Animal:
    def speak(self):
        print("...")

class Dog(Animal):
    def speak(self):   # Override!
        print("Woof!")

class Cat(Animal):
    def speak(self):   # Override!
        print("Meow!")

animals = [Dog(), Cat(), Dog()]
for animal in animals:
    animal.speak()   # Each uses its own version of speak()
# Woof! Meow! Woof!
```

This is called **polymorphism** — the same method name does different things depending on the object's type.

---

## `super()` — Calling the Parent's Method

Use `super()` to call the parent class's version of a method:

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # Call Animal's __init__
        self.breed = breed            # Add Dog-specific attribute

dog = Dog("Buddy", 3, "Labrador")
print(dog.name, dog.breed)   # Buddy Labrador
```

---

## Polymorphism in Action

```python
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6), Circle(3)]

for shape in shapes:
    print(f"Area: {shape.area():.2f}")
# Area: 78.54
# Area: 24.00
# Area: 28.27
```

The beauty: you can add `Triangle` or `Hexagon` without changing the loop.

---

## `isinstance()` and `issubclass()`

```python
dog = Dog("Buddy", 3, "Labrador")

print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True — Dog IS-A Animal
print(isinstance(dog, Cat))     # False

print(issubclass(Dog, Animal))  # True
```

---

## 📺 Watch These

1. **Python OOP: Inheritance** — Corey Schafer
   👉 [https://www.youtube.com/watch?v=RSl87lqOXDE](https://www.youtube.com/watch?v=RSl87lqOXDE)

2. **Inheritance and Polymorphism** — CS Dojo
   👉 [https://www.youtube.com/watch?v=Cn7AkDb4pIU](https://www.youtube.com/watch?v=Cn7AkDb4pIU)

---

## Key Takeaways

- **Inheritance**: child classes inherit attributes and methods from parent classes
- **Override**: redefine a method in the child to change its behavior
- **`super()`**: call the parent's version of a method
- **Polymorphism**: the same method name works differently for different types
- `isinstance(obj, Class)` checks if an object is an instance of a class (or its parent)

---

*Next up → [Encapsulation & Dunder Methods](./03_encapsulation_dunders.md)*
