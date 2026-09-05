# day 21 of solving problems

# 1. Find missing number in the given array
def find_missing_number(arr:list):
    arrLength:int = len(arr)
    missing_arr:list = []

    for i in range(1, arrLength + 1):
        if i not in arr:
            missing_arr.append(i)

    print(f"The missing numbers are {missing_arr}");
find_missing_number([1, 2, 3, 5, 6, 8, 9]);



# 2. move all negative numbers to the begining of the array
def move_negative_numbers(arr:list):

    for i in arr:
        if i < 0:
            arr.remove(i)
            arr.insert(0, i)

    print(arr);
move_negative_numbers([-1, 2, -3, 4, 5, -6, 7, 8, -9]);