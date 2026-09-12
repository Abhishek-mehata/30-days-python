# day 28 of python problem solving

# 1. find intersection of two arrays
# approach 1
# time complexicity O(n^2)
# space complexicity O(1)
def find_intersection(arr1: list, arr2: list):
    new_arr:list = [];
    
    for i in arr1:
        for j in arr2:
            if i == j:
                new_arr.append(i)
    
    print(new_arr)
find_intersection([1,2,34,45], [45])

# approach 2
def bubble_sort(arr: list):
    n:int = len(arr);
    
    for i in range(0,n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                temp:int = arr[i]
                arr[i] = arr[j]
                arr[j] = temp;
    return arr;

def remove_duplicates(arr: list):
    new_arr:list = [];
    
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr;

def find_intersection_2(arr1: list, arr2: list):
    new_arr:list = [];
    
    # sort arr1
    s1:list = bubble_sort(arr1);
    # sort arr2
    s2:list = bubble_sort(arr2);
    
    # remove duplicates from arr1
    s1 = remove_duplicates(s1);
    s2 = remove_duplicates(s2);
    
    for i in s1:
        for j in s2:
            if i == j:
                new_arr.append(i)
    print(new_arr);
find_intersection([1,2,3],[1,4,5,4])

# approach 3
# Time:  O(n + m) average
# Space: O(m)
def find_intersection_optimized(arr1: list, arr2: list):
    data:set = set(arr1)
    new_arr:list = [];
    
    for i in arr2:
        if i in data:
            new_arr.append(i)
            data.remove(i)  # Remove to avoid duplicates

    print(new_arr)
find_intersection_optimized([1,2,3],[1,4,5,4])
















# 2. Find the Largest Sum Subarray
# Subarray = elements next to each other

# [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#  ↑
# start here

# [-2]
# [-2, 1]
# [-2, 1, -3]
# [-2, 1, -3, 4]
# ...

def largest_subarray_sum(arr: list):
    
    if len(arr) == 0:
        print(0)
        return
    
    max_sum:int = arr[0]
    current_sum:int = arr[0]
    
    for i in range(1,len(arr)):
        current_sum += arr[i];
        
        if current_sum >max_sum:
            max_sum = current_sum;
        if current_sum < 0:
            current_sum = 0;
    print(max_sum)
largest_subarray_sum([-2,1,-3,4,-1,2,1,-5,4])












# 3. find the majority element in an array
def find_majority_element(arr: list):
    n:int = len(arr)
    
    data:dict = {}
    
    for i in arr:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1
    
    largest = {
        "value":0,
        "frequency":0
    };
    for key in data:
        # count:int = 0

        
        key_frequency:int = data[key]
        
        if key_frequency > largest["frequency"]:
            largest["value"] = key
            largest["frequency"] = key_frequency
            
    print(largest["value"])

find_majority_element([1,2,3,4,4,4,4,4,6]);
