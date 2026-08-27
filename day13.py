# day 13 of python problem solving

# 1. Find the most frequent element in an array
def find_repeating(arr:list):
    data:dict = {}
    
    for i in arr:
        if i in data:
            data[i] = data[i] + 1
        else:
            data[i] = 1
    
    # print(data)
    
    # largest_elem:dict = {}
    largest_flag:int = 0
    largest_elem = None
    
    for key in data:
        if data[key] > largest_flag:
            # largest_flag = key
            largest_flag = data[key]
            largest_elem = key
    
    print(largest_elem)
find_repeating([1, 2, 2, 3, 1, 2, 4])


# 2. Move all negative numbers to the beginning
def move_negative_at_begining(arr:list):
    new_List:list = []
    for i in arr:
        if(i>0 or i==0):
            new_List.append(i)
        elif i<0:
            new_List.insert(0,i)
    print(new_List)

move_negative_at_begining([2, -1, 4, -3, 5, -2])


