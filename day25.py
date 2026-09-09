# day 25 of python problem solving

# 1. find difference between two arrays
def find_difference(arr1: list, arr2: list):
    difference_arr:list = [];
    
    # check elements for arr1
    for i in arr1:
        if i not in arr2 and i not in difference_arr:
            difference_arr.append(i)
    
    # check elements for arr2
    for j in arr2:
        if j not in arr1 and j not in difference_arr:
            difference_arr.append(j);
    
    print(difference_arr);
find_difference([1, 2, 3, 4], [2, 4, 6, 8])


# 2. check if two arrays are equal
def check_arrays(arr1: list, arr2: list):
    
    if len(arr1) != len(arr2):
        print("Arrays are not equal")
        # return;
        return;
    
    for i in range(0,len(arr1)):
        if arr1[i] != arr2[i]:
            print("Arrays are not equal")
            return;

    print("Arrays are equal")
check_arrays([1, 2, 3, 4], [1, 2, 3, 4])