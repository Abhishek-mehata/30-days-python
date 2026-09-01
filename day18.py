# day 18 of python problem solving

# 1. Find the Majority Element
# Given an array, find the element that appears more than n / 2 times, where n is the length of the array.
def find_majority_element(arr:list ):
    n = len(arr)
    majority_repeating_flag = n//2

    data:dict = {}
    for i in arr:
        if i in data:
            data[i] = data[i] + 1
        else:
            data[i] = 1
    
    newArr:list = []
    for key in data:
        if data[key] > majority_repeating_flag:
            # newArr.append(key)
            print(key)
            return;
    return None;

find_majority_element([2, 2, 1, 2, 3, 2, 2])



# Given an unsorted array of integers, find the length of the longest sequence of consecutive numbers.
# Example
# :arr = [100, 4, 200, 1, 3, 2]
# # Output:
# 4

# # 2. Find the Longest Consecutive Sequence

# Approach 1
def bubble_sort(arr:list):
    arrLength = len(arr);
    
    for i in range(0, arrLength):
        for j in range(0, arrLength - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr;

def find_the_longest_consecutive(arr:list):
    
    sorted_arr = bubble_sort(arr);
    longest=1;
    current=1;
    

    for i in range(0, len(sorted_arr) - 1):
        
        if sorted_arr[i] + 1 == sorted_arr[i+1]:
            current += 1;
            
            if current > longest:
                longest = current;
        elif sorted_arr[i] == sorted_arr[i+1]:
            continue;
        else:
            current = 1;
    return longest;
print(find_the_longest_consecutive([100, 4, 200, 1, 3, 2]))



# Approach 2
def find_the_longest_consecutive_2(arr:list):
    arr_set = set(arr);
    longest = 0;
    
    for num in arr_set:
        
        if num - 1 not in arr_set:
            current_num = num;
            current_streak = 1;
            
            # Find consecutive numbers
            while current_num + 1 in arr_set:
                current_num += 1
                current_streak+=1;
            
            if current_streak > longest:
                longest = current_streak;
    return longest;

print(find_the_longest_consecutive_2([5,3,1,2]))