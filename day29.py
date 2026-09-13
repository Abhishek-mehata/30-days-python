# day 29 of python problem solving

# find the first non repeating element
# Time complexity: O(n)
# Space complexity: O(n)
def first_non_repeating(arr: list):
    n:int = len(arr)
    count:int = 0
    
    data:dict = {}
    
    for i in arr:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1
    
    for key in data:
        if data[key] == 1:
            print(key)
            return;
first_non_repeating([1,1,2,3,4,4,])


# 2. Find the pair with a given sum
# Input:  [2, 7, 11, 15]
# Target: 9
# Output: [2, 7]

# approach 1: Brut Force
# Time complexity: O(n^2)
# Space complexity: O(1)
def find_pair_with_sum(arr: list, target: int):
    n:int = len(arr);
    
    for i in range(0,n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                print([arr[i], arr[j]]);
                return;
find_pair_with_sum([2, 7, 11, 15], 9)



# aproach 2: Dictionary
# Time complexity: O(n)
# Space complexity: O(n)
def find_pair_with_sum_2(arr: list, target: int):
    n:int = len(arr)
    data:dict = {}
    
    for i in arr:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1
    
    for i in arr:
        if (target - i) in data:
            print([i, (target - i)])
            return
find_pair_with_sum_2([2, 7, 11, 15], 9)

















# 3. Move all negative numbers to the left
# Time complexity: O(n^2)
# Space complexity: O(1)
def move_all_negative_to_left(arr: list):
    n:int = len(arr)
    
    for i in range(0, n):
        if arr[i] < 0:
            arr.insert(0, arr.pop(i));
    
    print(f"Array after moving negative numbers to left {arr}")
move_all_negative_to_left([1,2,3,-4,5,-9]);





# Approach 2: Two pointer / partition approach

# j represents the position where the next negative
# element should be placed.
#
# i traverses through the array.
#
# When a negative element is found, swap it with arr[j]
# and move j to the next position.
#
# Time complexity: O(n)
# Space complexity: O(1)
def move_all_negative_to_left_2(arr: list):
    n:int = len(arr)
    
    # flag where -ve elements will be added
    j:int = 0
    
    for i in range(0,n):
        if arr[i] < 0:
            temp:int = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1;
    print(f"More optimized method of moving -ve nums to left {arr}")
move_all_negative_to_left_2([1,2,3,-4,5,-9])