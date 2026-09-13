# day 30 of python problem solving

# Problem: Find the longest consecutive sequence
# Given an unsorted array of integers, find the length of the longest sequence of consecutive numbers.

arr = [100, 4, 200, 1, 3, 2]
# Output:
4
# Because:
# 1, 2, 3, 4



def bubble_sort(arr: list):
    n:int = len(arr)
    
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                temp:int = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    # print(arr)
    return arr
# bubble_sort([1,3,2,5,4,7,6])

def longest_consecutive_sequence(arr: list):
    long_arr:list = []
    current_arr:list = []
    
    n:int = len(arr)
    arr = bubble_sort(arr=arr)
    
    current_consecutive_length:int = n
    for i in range(0,n-1):
        if i == 0:
            current_arr.append(arr[i]);
        elif arr[i] == arr[i-1] + 1:
            current_arr.append(arr[i])
        else:
            if len(current_arr) > len(long_arr):
                long_arr = current_arr
            current_arr = [arr[i]]
    
    if len(current_arr) > len(long_arr):
        long_arr = current_arr
    
    print(long_arr)
longest_consecutive_sequence([100, 4, 200, 1, 3, 2]);