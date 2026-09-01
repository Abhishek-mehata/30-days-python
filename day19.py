# day 19 of python problem solving


# 1. Linear Search
def linear_search(arr:list, target:int):
    for i in range(0, len(arr)):
        if arr[i] == target:
            print(f"The element found at the position {i+1} . index {i}")
            return;
    print("Element not found")
linear_search([10, 25, 7, 42, 15],42)

# 2. Binary Search
def binary_search(arr:list, target:int ):
    low:int = 0
    high:int = len(arr) - 1

    while low <= high:
        mid:int = (low + high) // 2

        if arr[mid] == target:
            print(f"The element found at the position {mid+1} . index {mid}")
            return
        elif arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1;
binary_search([10, 25, 7, 42, 15],42)


# 3. bubble sort algorithm
def bubble_sort(arr:list):
    arrLength = len(arr)

    for i in range(0, arrLength):
        for j in range(0,arrLength-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # return arr;
    print(arr)
bubble_sort([5, 2, 9, 1, 5, 6])