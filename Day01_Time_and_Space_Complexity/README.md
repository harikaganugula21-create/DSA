# 📘 Day 1 - Time and Space Complexity

## 📖 What is Time Complexity?

Time Complexity is the amount of time an algorithm takes to execute as the input size increases.

## 📖 What is Space Complexity?

Space Complexity is the amount of memory (RAM) used by an algorithm during execution.

**Formula:**

Space Complexity = Input Space + Auxiliary Space

- **Input Space:** Memory required to store the input.
- **Auxiliary Space:** Extra memory used by the algorithm.

---

## 📌 Big O Notation

Big O Notation is used to measure the efficiency of an algorithm.

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Array Access |
| O(log n) | Logarithmic | Binary Search |
| O(n) | Linear | Single Loop |
| O(n log n) | Linearithmic | Merge Sort |
| O(n²) | Quadratic | Nested Loops |
| O(2ⁿ) | Exponential | Recursive Problems |

---

## 💻 Examples

### O(1) - Constant Time

```python
arr = [10, 20, 30]
print(arr[1])
```

### O(n) - Linear Time

```python
for i in range(n):
    print(i)
```

### O(n²) - Quadratic Time

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

---

## 🔄 Difference Between Time & Space Complexity

| Time Complexity | Space Complexity |
|-----------------|------------------|
| Measures execution time | Measures memory usage |
| Depends on number of operations | Depends on memory used |
| Goal is faster execution | Goal is less memory usage |

---

## ✅ Applications

- Searching Algorithms
- Sorting Algorithms
- Artificial Intelligence
- Machine Learning
- Database Management
- Operating Systems
- Computer Networks
- Game Development
