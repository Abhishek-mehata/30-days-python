# day 24 of python problem solving


# find intersection of two arrays

# approach 1
# time complexicity O(n²)
# space complexicity O(n)
def find_intersection(arr1: list, arr2: list):
    intersection_arr:list = []
    for i in arr1:
        for j in arr2:
            if i==j:
                intersection_arr.append(i);
    print(intersection_arr);
find_intersection([1, 2, 3, 4], [2, 4, 6, 8])

# approach 2
# time complexicity O(n)
# space complexicity O(n)
def find_intersection_2(arr1: list, arr2: list):
    intersection_data:dict = {}
    intersection_arr:list = []
    
    for i in arr1:
        if i not in intersection_data:
            intersection_data[i] = 1
    
    for j in arr2:
        if j in intersection_data:
            intersection_arr.append(j)
    
    print(intersection_arr);
find_intersection_2([1, 2, 3, 4], [2, 4, 6, 8])



# ------------------------------------------------------------------

# 2. find first non repeating element in an array
def find_first_non_repeating(arr: list):
    data:dict = {};
    
    for i in arr:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1
    
    for key in data:
        if data[key] == 1:
            print(key)
            return;

find_first_non_repeating([4, 5, 1, 2, 1, 4, 5]);