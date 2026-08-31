# day 15 of python problem solving

# 1. find first duplicate
def find_first_duplicate(arr:list):
    arrLength:int = len(arr)
    
    for i in range(0, arrLength):
        for j in range(i+1, arrLength):
            if(arr[i] == arr[j]):
                # duplicate = arr[i]
                print(f"The duplicate is {arr[i]}")
                # break;
                return;

find_first_duplicate([2, 1, 3, 5, 3, 2])


# 2. find two numbers with largest sum
def find_two_with_largest_sum(arr:list):
    sumArr:list=[];
    largestSum:int = arr[0] + arr[1]
    
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            sumArr.append(arr[i]+arr[j])
    
    for i in sumArr:
        if i > largestSum:
            largestSum = i
    print(largestSum)
find_two_with_largest_sum([10, 5, 20, 8, 15])