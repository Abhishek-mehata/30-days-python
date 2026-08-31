# day 17 of python problem




# 1. Find the First Repeating Element
# Approach 1
# Time complexicity -> O(n^2)
# Space complexicity -> O(1)
def find_first_repeating(arr:list):
    arrLength:int = len(arr)
    for i in range(0, arrLength):
        for j in range(i+1 , arrLength ):
            if arr[i] == arr[j]:
                print(f"The first repeating element is {arr[i]}")
                return;
find_first_repeating([10, 5, 3, 4, 3, 5, 6])

# Approach 2
# time complexicity 2O(n) -> O(n) + O(n) -> O(n)
# space complexicity O(n)
def find_initial_repeating(arr:list):
    data:dict = {}
    
    for i in arr:
        if i in data:
            data[i] = data[i] + 1
        else:
            data[i] = 1
    
    for key in data:
        if data[key] >= 2:
            print(f"{key} is the first repeating element in given array {data[key]} times");
            return;
    
find_initial_repeating([10, 5, 3, 4, 3, 5, 6])



# 2. Find the last element in the array that appears only once.
# time complexicity -> O(n^2)
# space complexicity -> O(n)
def find_last_unique(arr:int):
    arrLength:int =len(arr);
    
    for i in range(arrLength-1, -1, -1):
        count=0
        for j in range(0, arrLength):
            if arr[i] == arr[j]:
                count += 1;
        if(count == 0):
            print(f"The last unique element is {arr[i]}");
            return;
find_last_unique([1, 2, 3, 3, 5, 6])

