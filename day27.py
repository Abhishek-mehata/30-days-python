# day 27 of python problem solving

# 1. Find the Missing Number
# Input:  [3, 0, 1]
# Output: 2

# Input:  [0, 1]
# Output: 2

# Input:  [9, 6, 4, 2, 3, 5, 7, 0, 1]
# Output: 8
def bubble_sort(arr: list):
    n:int  = len(arr)
    
    if n == 0:
        return arr
    
    for i in range(0,n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                temp:int = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr;

# time complexicity O(n^2)
# space complexicity O(n)
def find_missing_number(arr: list):
    sorted_arr:list = bubble_sort(arr);
    n:list=len(sorted_arr)
    missing_arr:list = [];

    for i in range(0,n):
        if i != sorted_arr[i]:
            missing_arr.append(i)
            break;
    else: # this else will be executed when the if block of loop gets false
        missing_arr.append(n)
    print(f"The Missing number is {missing_arr[0]}")


# find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]);
find_missing_number([0, 1, 2]);










# # 2. Move All Negative Numbers to the Left

# approach 1
# time complexicity O(n²)
# space complexicity O(1)
def move_negative_numbers(arr: list):
    n:int = len(arr)
    
    if n == 0:
        return arr;
    
    for i in range(0,n):
        if arr[i] < 0:
            arr.insert(0, arr.pop(i));
            # arr.insert -> O(n) and arr.pop -> O(n)
            # both operation happen one after another
            # O(n) + O(n) = O(2n) = O(n)
            # since this operation is inside a loop:
            # O(n) * O(n) = O(n²)
            
    print(f"Array after moving negative numbers to the left is {arr}")
move_negative_numbers([-1, 2, -3, 4, 5, -6, 7, 8, -9]);



# approach 2
def move_negative_numbers_2(arr: list):
    n:int = len(arr);
    
    j:int = 0; # index flag where the first -ve element will be placed
    
    for i in range(0,n):
        if arr[i] < 0:
            temp:int = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1
            
    print(f"Moved -ve numbers at begining {arr}");
move_negative_numbers_2([1,2,3,-1,-2,-44]);
















# 3. Find the First Non-Repeating Element

# approach 1
# time complexiity O(n^2)
# space complexicity O(n)
def find_first_non_repeating_element(arr: list):
    n:int = len(arr)
    
    if n == 0:
        return arr;
    
    for i in range(0,n):
        
        count:int = 0;
        
        for j in range(0,n):
            if arr[i] == arr[j]:
                # print(f"First non-repeating element is {arr[i]}")
                count += 1;
                # return;
        if count == 1:
            print(f"First non-repeating element is {arr[i]}")
            return;
find_first_non_repeating_element([9, 4, 9, 6, 7, 4, 6, 8, 7]);



# approach 2
# time complexicity O(n)
# space complexicity O(n)
def find_first_non_repeating_element_2(arr: list):
    n:int = len(arr)
    
    if n == 0:
        return arr;
    
    
    data:dict  = {};
    for i in arr:
        if i in data:
            data[i] +=1;
        else:
            data[i] = 1
    
    for key in data:
        if data[key] == 1:
            print(f"The first non repeating element is {key}");

find_first_non_repeating_element_2([4, 5, 1, 2, 1, 4, 5])