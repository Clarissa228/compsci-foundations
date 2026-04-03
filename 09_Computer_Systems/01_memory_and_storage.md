# Memory & Storage

## The Memory Hierarchy

Computers have multiple types of storage, each trading off **speed** vs **size** vs **cost**:

```
  Registers       ← Fastest, smallest (bytes), inside CPU
  CPU Cache (L1/L2/L3)   ← Very fast (KB-MB), inside/near CPU
  RAM             ← Fast (GB), main working memory
  SSD/Hard Drive  ← Slower (TB), permanent storage
  Network/Cloud   ← Slowest, unlimited, remote
```

As you go down: slower, cheaper, larger, and more persistent.

---

## RAM — Random Access Memory

RAM is your computer's **working memory** — it holds everything currently running:
- Open applications
- Browser tabs
- Files being edited

When RAM fills up, the OS starts using the hard drive as "virtual memory" — which is *much* slower. This is why your computer slows down when you have too many programs open.

**Key properties**:
- **Volatile**: cleared when power is off
- **Random access**: any address accessed in O(1) time
- Typically 8–32 GB in modern computers

---

## How Python Stores Variables

When you write `x = 42`, Python:
1. Allocates a block of memory for the integer 42
2. Stores the **address** (memory location) in the variable `x`
3. When you use `x`, Python follows that address to get the value

This is called a **reference** or **pointer**.

```python
a = [1, 2, 3]
b = a         # b points to the SAME list as a!

b.append(4)
print(a)      # [1, 2, 3, 4]  — a changed too!
```

This is why copying mutable objects requires care:
```python
import copy
c = copy.copy(a)     # Shallow copy
d = copy.deepcopy(a) # Deep copy (for nested structures)
```

---

## The Stack and the Heap

Python (and most languages) manage memory in two regions:

### The Stack
- Stores **function calls and local variables**
- Automatically managed — variables disappear when a function returns
- Fast allocation and deallocation
- Limited in size (deep recursion can overflow it — `RecursionError`)

### The Heap
- Stores **objects** (lists, dicts, class instances)
- Managed by Python's **garbage collector**
- Large and flexible

When you write `x = [1, 2, 3]`:
- The variable `x` lives on the **stack** (it's a local reference)
- The actual list `[1, 2, 3]` lives on the **heap**

---

## Garbage Collection

Python automatically reclaims memory that's no longer needed — called **garbage collection**.

```python
def make_list():
    big_list = list(range(1_000_000))   # Allocated on heap
    return big_list[0]
    # big_list goes out of scope here — Python will free its memory

result = make_list()
# big_list's memory is now freed
```

Python uses **reference counting**: each object tracks how many variables point to it. When the count drops to zero, the memory is freed.

---

## How Storage Works

**SSDs and HDDs** store data as files organized in a **file system**:
- A file system is a tree structure (directories/folders contain files and other directories)
- Files have metadata: name, size, creation date, permissions
- OS manages reading/writing through a driver

```
/ (root)
├── Users/
│   └── Alice/
│       ├── Documents/
│       └── Desktop/
├── Applications/
└── System/
```

---

## 📺 Watch These

1. **How RAM Works** — Computerphile
   👉 [https://www.youtube.com/watch?v=fpnE6UAfbtU](https://www.youtube.com/watch?v=fpnE6UAfbtU)

2. **Stack vs Heap Memory** — Programming with Mosh
   👉 [https://www.youtube.com/watch?v=_8-ht2AKyH4](https://www.youtube.com/watch?v=_8-ht2AKyH4)

---

## Key Takeaways

- Memory hierarchy: Registers → Cache → RAM → Storage (fast to slow)
- RAM is fast and temporary; storage is slow and permanent
- Python variables are **references** (pointers) to objects on the heap
- The **stack** holds function calls; the **heap** holds objects
- Python's **garbage collector** automatically frees unused memory

---

*Next up → [Operating Systems](./02_operating_systems.md)*
