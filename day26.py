# day 26 of python problem solving

# 1. Find the Union of Two Arrays
# time complexicity is O(n)
# space complexicity is O(n)
def find_union(arr1: list, arr2: list):
    union_arr:list = [];
    
    # check elements for arr1
    for i in arr1:
        if i not in union_arr:
            union_arr.append(i);
    
    for j in arr2:
        if j not in union_arr:
            union_arr.append(j);
            
    print(union_arr);
find_union([1,2,3,4],[5,6,7,8]);


# 2. Find the Element That Appears Once
# time complexicity is O(n)
# space complexicity is O(n)
def find_first_appearence(arr: list):
    data:dict = {};
    
    for i in arr:
        if i in data:
            data[i] = data[i] + 1;
        else:
            data[i] = 1
    
    final_arr:list = [];
    
    for key in data:
        if data[key] == 1:
            final_arr.append(key)
    print(final_arr)
find_first_appearence([1,2,3,3,4,4,5,6,6,7]);