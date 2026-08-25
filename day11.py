# day 11 of solving problems
# [1,2,3,4,0,5]

# move all zeros at end
def move_zeros_to_end(arr:list):
    zeroArr:list = []
    nonZeroArr:list=[]
    
    for i in arr:
        if i == 0:
            zeroArr.append(0)
        else:
            nonZeroArr.append(i)
    newArr:list = nonZeroArr + zeroArr
    print(newArr)
move_zeros_to_end([0, 1, 0, 3, 12])



# one number is always missing
def find_missing_number(arr:list):
    missing_array:list = [];
    
    n:int = len(arr) + 1;
    

    if(arr[0] != 1):
        missing_array.append(1);
    
    for i in range(0, len(arr) - 1):
        if(arr[i+1] != arr[i]+1):
            missing_array.append(arr[i]+1);
    
    if arr[-1] != n:
        missing_array.append(n)
    print(missing_array)
find_missing_number([1, 2, 3, 4, 5])