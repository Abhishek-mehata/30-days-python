# day 23 of python problem solving

# 1. Given an array, find the first element that repeats

# approach 1
def find_first_repeating(arr: list):
    arrLength:int = len(arr);
    
    for i in range(0, arrLength):
        for j in range(i+1, arrLength):
            if arr[i] == arr[j]:
                print(arr[i]);
                return;

find_first_repeating([10, 5, 3, 4, 3, 5, 6])

# approach 2
def find_first_repeating_2(arr: list):
    data:dict = {}
    
    for i in range(0, len(arr)):
        if arr[i] in data:
            data[arr[i]] += 1
        else:
            data[arr[i]] = 1
    
    for key in data:
        if data[key] >= 2:
            print(key)
            return;
find_first_repeating_2([10, 5, 3, 4, 3, 5, 6])


# 2. Check if Two Arrays Are Equal
# check weather two arrays contain the same elements with the same frequencies, regardless of order
def check_arrays(arr1: list, arr2: list):
    data_arr1:dict = {}
    data_arr2:dict = {}
    
    isEqual:bool = True
    
    # structurizing the list 1
    for i in arr1:
        if i in data_arr1:
            data_arr1[i] += 1
        else:
            data_arr1[i] = 1
    
    # structurizing the list 2
    for j in arr2:
        if j in data_arr2:
            data_arr2[j] += 1
        else:
            data_arr2[j] = 1
    
    for key in data_arr1:
        if key not in data_arr2 or data_arr1[key] != data_arr1[key]:
            isEqual=False
            break
    
    if isEqual:
        print("Equal")
    else:
        print("Not equal");

check_arrays([1, 2, 3, 4, 2], [2, 4, 3, 2, 1])
