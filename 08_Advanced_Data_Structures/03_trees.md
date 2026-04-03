# Trees

## The Big Idea

A **tree** is a hierarchical data structure — unlike lists and linked lists which are linear. Trees are everywhere: file systems, HTML DOM, company org charts, decision trees in AI.

```
         10
        /  \
       5    15
      / \     \
     3   7    20
```

---

## Key Terminology

- **Root** — the top node (10 above)
- **Node** — any element in the tree
- **Parent/Child** — a node directly above/below another
- **Leaf** — a node with no children (3, 7, 20)
- **Height** — the number of levels
- **Subtree** — a node and all its descendants

---

## Binary Tree

A **binary tree** is a tree where each node has **at most 2 children** (left and right).

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

---

## Binary Search Tree (BST)

A **BST** is a binary tree with a special property:
- All values in the **left subtree** are **less than** the node
- All values in the **right subtree** are **greater than** the node

This allows O(log n) search!

```python
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return TreeNode(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        return node

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)


tree = BST()
for val in [10, 5, 15, 3, 7, 20]:
    tree.insert(val)

print(tree.search(7))   # True
print(tree.search(8))   # False
```

---

## Tree Traversals

How you "visit" every node in a tree. There are 3 main orders:

### In-Order (Left → Node → Right)
Visits nodes in **sorted order** for a BST:
```python
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)    # Visit
        inorder(node.right)
```
Output for our tree: `3, 5, 7, 10, 15, 20`

### Pre-Order (Node → Left → Right)
Used for copying or serializing trees:
```python
def preorder(node):
    if node:
        print(node.data)    # Visit first
        preorder(node.left)
        preorder(node.right)
```

### Post-Order (Left → Right → Node)
Used for deletion or calculating tree properties:
```python
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)    # Visit last
```

---

## Height of a Tree

```python
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))
```

---

## BST vs Hash Table

| | BST | Hash Table (dict) |
|--|-----|------|
| Search | O(log n) avg | O(1) avg |
| Sorted order? | ✅ Yes | ❌ No |
| Range queries? | ✅ Easy | ❌ Hard |
| Worst case | O(n) unbalanced | O(n) rare |

---

## 📺 Watch These

1. **Binary Trees and BST** — CS Dojo
   👉 [https://www.youtube.com/watch?v=hWokyBoo0aI](https://www.youtube.com/watch?v=hWokyBoo0aI)

2. **Tree Traversals** — William Fiset
   👉 [https://www.youtube.com/watch?v=k7GkEbECZK0](https://www.youtube.com/watch?v=k7GkEbECZK0)

---

## Key Takeaways

- A tree is a **hierarchical** structure with a root, branches, and leaves
- A **BST** keeps values ordered: left < node < right — enables O(log n) search
- The three traversals — in-order, pre-order, post-order — each have specific uses
- Almost all tree algorithms use **recursion** naturally

---

*Next up → [Graphs](./04_graphs.md)*
