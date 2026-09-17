# 📘 Day 2 - Arrays & Memory Representation

## 📖 What is an Array?

An array is a linear data structure that stores multiple elements of the same data type in contiguous memory locations.

An array allows direct access to elements using an index.

### Example

```python
arr = [10, 20, 30, 40, 50]
```

- arr[0] = 10
- arr[1] = 20
- arr[2] = 30
- arr[3] = 40
- arr[4] = 50

---

# 🔹 Characteristics of an Array

- Stores elements of the same type.
- Elements are stored in contiguous memory locations.
- Each element has an index.
- Index starts from 0.
- Random access is possible.

---

# 📌 Memory Representation of an Array

Suppose we have:

```python
arr = [10, 20, 30, 40, 50]
```

Memory representation:

```
Index:    0     1     2     3     4

Value:   10    20    30    40    50

Address:
1000   1004   1008   1012   1016
```

Each integer occupies **4 bytes**, so the addresses increase by **4 bytes**.

---

# 📌 Address Formula

Address of an element:

```
Address = Base Address + (Index × Size of Data Type)
```

Example:

- Base Address = 1000
- Index = 3
- Size = 4 bytes

Address of arr[3]

```
1000 + (3 × 4)

= 1012
```

---

# 📌 Advantages of Arrays

- Fast access using index.
- Easy to traverse.
- Memory efficient.
- Simple implementation.

---

# 📌 Disadvantages of Arrays

- Fixed size (in many programming languages).
- Insertion is costly.
- Deletion is costly.
- Stores similar data types.

---

# 📌 Applications of Arrays

- Searching
- Sorting
- Matrices
- Stacks
- Queues
- Dynamic Programming

---

# 📌 Time Complexity

| Operation | Complexity |
|-----------|------------|
| Access | O(1) |
| Search | O(n) |
| Update | O(1) |
| Insert | O(n) |
| Delete | O(n) |

---

# ✅ Summary

- Array is a linear data structure.
- Stores elements in contiguous memory.
- Uses indexing.
- Fast element access.
- Insertion and deletion take more time.