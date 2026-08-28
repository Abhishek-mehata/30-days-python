# day 14 of python problem solving

# 1. find the second most frequent elemnent in an array
def find_second_frequent(arr:list):
    data:dict = {}
    
    for i in arr:
        if i in data:
            data[i] = data[i] + 1;
        else:
            data[i] = 1

    largest_frequency = 0
    largest_target = None
    
    second_largest_frequency = 0
    second_largest_target = None
    
    for key in data:
        frequency = data[key]
        
        if frequency > largest_frequency:
            second_largest_frequency = largest_frequency
            second_largest_target = largest_target
            
            largest_frequency = frequency
            largest_target = key
            
        elif frequency > second_largest_frequency and frequency < largest_frequency:
            second_largest_frequency = frequency
            second_largest_target = key

    print(f"The element {second_largest_target} repeats second largest times {second_largest_frequency}")
            
        
find_second_frequent([1, 2, 2, 3, 3, 3, 4, 4])



# 2. find intersection of two arrays
# Input:
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [3, 4, 5, 6, 7]

# Output:
# [3, 4, 5]

def intersection(arr1:list , arr2:list):
    intersection_array:list = []
    
    for i in arr1:
        for j in arr2:
            if(i==j):
                intersection_array.append(i)
    print(intersection_array)
intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])