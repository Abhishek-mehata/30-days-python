# Day 19 — Python Problem Solving

## 🎯 Focus

Today was a **fundamentals reinforcement day**.

The goal was to write three core algorithms from memory:

1. Linear Search
2. Binary Search
3. Bubble Sort

The main focus was building **algorithm muscle memory** rather than learning new concepts.

---

# 1. 🔎 Linear Search

Linear Search checks every element one by one until the target is found.

### Code

```python
def linear_search(arr: list, target: int):

    for i in range(0, len(arr)):

        if arr[i] == target:

            print(f"The element found at the position {i + 1}. index {i}")

            return

    print("Element not found")


linear_search([10, 25, 7, 42, 15], 42)
```

### Example

```text
Array:  [10, 25, 7, 42, 15]
Target: 42

Position: 4
Index:    3
```

### Complexity

```text
Time:  O(n)
Space: O(1)
```

### Key Idea

```text
Start from the beginning
        ↓
Check current element
        ↓
Found?
 ┌──────┴──────┐
YES           NO
 ↓              ↓
Return       Check next
```

---

# 2. ⚡ Binary Search

Binary Search repeatedly divides a **sorted array** into two halves.

### Important Requirement

> ⚠️ Binary Search requires the array to be sorted.

### Code

```python
def binary_search(arr: list, target: int):

    low: int = 0
    high: int = len(arr) - 1

    while low <= high:

        mid: int = (low + high) // 2

        if arr[mid] == target:

            print(f"The element found at the position {mid + 1}. index {mid}")

            return

        elif arr[mid] < target:

            low = mid + 1

        elif arr[mid] > target:

            high = mid - 1


binary_search([7, 10, 15, 25, 42], 42)
```

### How it works

```text
[7, 10, 15, 25, 42]
          ↑
         mid
```

If:

```text
target == middle
        ↓
      FOUND
```

If:

```text
target > middle
        ↓
Search RIGHT
```

If:

```text
target < middle
        ↓
Search LEFT
```

### Complexity

```text
Time:  O(log n)
Space: O(1)
```

### Important Lesson

During practice, Binary Search was initially tested with:

```python
[10, 25, 7, 42, 15]
```

This array is **not sorted**, which reminded us that algorithms have conditions/assumptions.

Correct:

```python
[7, 10, 15, 25, 42]
```

---

# 3. 🫧 Bubble Sort

Bubble Sort repeatedly compares adjacent elements and swaps them when they are in the wrong order.

### Code

```python
def bubble_sort(arr: list):

    arrLength = len(arr)

    for i in range(0, arrLength):

        for j in range(0, arrLength - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(arr)


bubble_sort([5, 2, 9, 1, 5, 6])
```

### Example

```text
Before:
[5, 2, 9, 1, 5, 6]

After:
[1, 2, 5, 5, 6, 9]
```

### The Important Operation

```python
arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

This swaps two adjacent elements.

### Complexity

```text
Time:  O(n²)
Space: O(1)
```

---

# 📊 Algorithm Comparison

| Algorithm     | Purpose                        |       Time |  Space |
| ------------- | ------------------------------ | ---------: | -----: |
| Linear Search | Find an element                |     `O(n)` | `O(1)` |
| Binary Search | Find an element in sorted data | `O(log n)` | `O(1)` |
| Bubble Sort   | Sort an array                  |    `O(n²)` | `O(1)` |

---

# 🧠 Day 19 Key Learnings

### 1. Linear Search

> Check elements one by one.

### 2. Binary Search

> Divide the search space in half repeatedly.

### 3. Bubble Sort

> Compare adjacent elements and swap them when necessary.

### 4. Algorithms have requirements

Binary Search is only valid when the data is appropriately **sorted**.

### 5. Repetition builds muscle memory

The goal of today's practice was not simply to memorize three algorithms.

It was to reach the point where the basic structure naturally comes to mind:

```text
Linear Search
    ↓
loop → compare → found

Binary Search
    ↓
low → high → mid → eliminate half

Bubble Sort
    ↓
compare → swap → repeat
```

---

# 🚀 Day 19 Status

* ✅ Linear Search
* ✅ Binary Search
* ✅ Bubble Sort
* ✅ Practiced algorithms from memory
* ✅ Reviewed time complexity
* ✅ Reviewed space complexity
* ✅ Understood Binary Search's sorted-array requirement

## 🔥 Day 19 Completed
