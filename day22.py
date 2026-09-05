# day 22 of python problem solving

# 1. find the duplicate numbers in an array

# approach 1
# time complexicity O(n²)
# space complexicity O(n)


def find_duplicate(arr:list):
    duplicate_arr:list = []
    arrLen = len(arr)
    
    for i in range(0, arrLen):
        for j in range(i+1, arrLen):
            if arr[i] == arr[j] and arr[i] not in duplicate_arr:
                duplicate_arr.append(arr[i])

    print(f"The duplicate numbers are {duplicate_arr}");
find_duplicate([1, 2, 3, 4, 5, 6,6]);

# approach 2
# Time complexicity O(n)
# space complexicity O(n)
def find_duplicate_2(arr:list):
    duplicate_data:dict = {}

    for i in arr:
        if i in duplicate_data:
            duplicate_data[i] += 1
        else:
            duplicate_data[i] = 1

    duplicate_arr:list = []
    
    for key in duplicate_data:
        if duplicate_data[key] > 1:
            duplicate_arr.append(key)
    print(duplicate_arr);
find_duplicate_2([1, 3, 4, 2, 2])




# 2. find intersection of two arrays
def find_intersection(arr1: list, arr2: list):
    merged_arr:list = []
    
    for i in arr1:
        for j in arr2:
            if i == j and i not in merged_arr:
                merged_arr.append(i)
    print(f"The intersection of given two arrays, {merged_arr}");
find_intersection([1, 2, 2, 3, 4], [2, 2, 4, 6]);