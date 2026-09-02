# day 20 of python problem solving

# 1. Find the Second Largest Element
# Time Complexity: O(n)
# Explanation:
# We loop through the array only one time.
# If the array has n elements, we perform at most n iterations.

# Space Complexity: O(1)
# Explanation:
# We only use a fixed number of extra variables.
# The amount of extra memory does not increase with array size.
def find_second_largest(arr:list):
    first:int = arr[0]
    second:int = arr[0]

    arrLength:int = len(arr)
    for i in range(0, arrLength):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] < first:
            second = arr[i]
    print(f"The second largest element is {second}");

find_second_largest([10, 5, 20, 8, 20, 15]);


# ----------------

# 2. Check if an Array is Sorted

# Approach 1 : bubble sort + comparision
# Time Complexity: O(n²)
# Explanation:
# Bubble Sort uses nested loops.
# For every element, we may compare it with many other elements.

# Space Complexity: O(n)
# Explanation:
# original_arr = arr.copy() creates a new copy of the array.
# Therefore, extra memory grows according to the size of the array.
def bubble_sort(arr:int):
    arrLength:int = len(arr)

    for i in range(0,arrLength):
        for j in range(0, arrLength-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr;

def check_sorted(arr:list):
    original_arr:list =arr.copy();
    sorted_arr = bubble_sort(arr);

    isSorted:bool = True

    arrLength = len(arr)

    for i in range(0, arrLength):
        if original_arr[i] != sorted_arr[i]:
            isSorted = False
    
    if isSorted:
        print(f"The array {arr} is sorted in ascending order")
    else:
        print(f"The array {arr} is not sorted in ascending order")
check_sorted([1, 2, 3, 4, 5,9,999,19])


# ----------------

# Approach 2
# Time Complexity: O(n)
# Explanation:
# We loop through the array only once.
# We compare each element with the next element.

# Space Complexity: O(1)
# Explanation:
# We do not create another array or data structure.
# The extra memory remains constant.
def check_sorted_2(arr:list):
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i+1]:
            print(f"The array {arr} is not sorted in ascending order")
            return
    print(f"The array {arr} is sorted in ascending order")