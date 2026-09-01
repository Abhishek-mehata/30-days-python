# Day 18 — Python Problem Solving

---

# 🧩 Problem 1: Find the Majority Element

## Problem

Given an array, find the element that appears **more than `n / 2` times**, where `n` is the length of the array.

Return `None` if no majority element exists.

### Example

```python
arr = [2, 2, 1, 2, 3, 2, 2]

# Output: 2
```

## Approach: Dictionary Frequency Counter

### Time Complexity: `O(n)`

### Space Complexity: `O(n)`

```python
def find_majority_element(arr: list):

    n = len(arr)

    majority_repeating_flag = n // 2

    data: dict = {}

    # Count the frequency of every element
    for i in arr:

        if i in data:
            data[i] += 1

        else:
            data[i] = 1

    # Find an element appearing more than n // 2 times
    for key in data:

        if data[key] > majority_repeating_flag:
            return key

    # No majority element found
    return None


# Test
print(find_majority_element([2, 2, 1, 2, 3, 2, 2]))
```

---

# 🧩 Problem 2: Find the Longest Consecutive Sequence

## Problem

Given an unsorted array of integers, find the length of the longest sequence of consecutive numbers.

### Example

```python
arr = [100, 4, 200, 1, 3, 2]

# Output: 4
```

The longest consecutive sequence is:

```text
1 → 2 → 3 → 4
```

---

# 🚶 Approach 1: Bubble Sort

First, sort the array using Bubble Sort. Then traverse the sorted array and count consecutive numbers.

### Time Complexity: `O(n²)`

### Space Complexity: `O(1)` auxiliary space

```python
def bubble_sort(arr: list):

    arr_length = len(arr)

    for i in range(arr_length):

        for j in range(arr_length - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def find_the_longest_consecutive(arr: list):

    # Handle empty array
    if not arr:
        return 0

    # Sort the array
    sorted_arr = bubble_sort(arr)

    longest = 1
    current = 1

    # Find the longest consecutive sequence
    for i in range(len(sorted_arr) - 1):

        # Consecutive numbers
        if sorted_arr[i] + 1 == sorted_arr[i + 1]:

            current += 1

            if current > longest:
                longest = current

        # Duplicate numbers
        elif sorted_arr[i] == sorted_arr[i + 1]:

            continue

        # Sequence breaks
        else:

            current = 1

    return longest


# Test
print(find_the_longest_consecutive([100, 4, 200, 1, 3, 2]))
```

---

# 🚀 Approach 2: Set-Based Optimal Solution

Instead of sorting, convert the array into a `set`.

The important idea is:

> Only start counting when the current number is the beginning of a sequence.

For example, for:

```text
1 → 2 → 3 → 4
```

We start counting from `1` because:

```python
1 - 1 not in arr_set
```

We do not start from `2`, `3`, or `4` because their previous numbers already exist.

### Time Complexity: `O(n)`

### Space Complexity: `O(n)`

```python
def find_the_longest_consecutive_2(arr: list):

    # Convert the array into a set
    arr_set = set(arr)

    longest = 0

    # Check every number
    for num in arr_set:

        # Only start if num is the beginning of a sequence
        if num - 1 not in arr_set:

            current_num = num
            current_streak = 1

            # Find consecutive numbers
            while current_num + 1 in arr_set:

                current_num += 1
                current_streak += 1

            # Update the longest sequence
            if current_streak > longest:

                longest = current_streak

    return longest


# Test
print(find_the_longest_consecutive_2([5, 3, 1, 2]))
```

---

# 📊 Complexity Comparison

| Approach                          | Time Complexity | Space Complexity |
| --------------------------------- | --------------- | ---------------- |
| Majority Element — Dictionary     | `O(n)`          | `O(n)`           |
| Longest Consecutive — Bubble Sort | `O(n²)`         | `O(1)` auxiliary |
| Longest Consecutive — Set         | `O(n)`          | `O(n)`           |

---

# 🎯 Key Learning From Day 18

Today was important because you learned that:

1. The same problem can have multiple solutions.
2. A correct solution is not always the most efficient solution.
3. Bubble Sort can solve the consecutive sequence problem, but it takes `O(n²)` time.
4. A `set` allows very fast membership checking.
5. Checking whether `num - 1` exists helps identify the beginning of a consecutive sequence.
6. Comparing **Time Complexity and Space Complexity** helps choose the better algorithm.

# 🔥 Day 18 Completed!
